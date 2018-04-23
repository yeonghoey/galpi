resource "aws_s3_bucket" "main" {
  bucket = "${var.bucket}"

  policy = <<EOF
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal": {"AWS": "${aws_cloudfront_origin_access_identity.main.iam_arn}"},
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::${var.bucket}"]
    },
    {
      "Effect":"Allow",
      "Principal": {"AWS": "${aws_cloudfront_origin_access_identity.main.iam_arn}"},
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::${var.bucket}/*"]
    }
  ]
}
EOF
}

resource "aws_cloudfront_distribution" "main" {
  origin {
    domain_name = "${aws_s3_bucket.main.bucket_domain_name}"
    origin_id   = "${var.bucket}"

    s3_origin_config {
      origin_access_identity = "${aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path}"
    }
  }

  default_cache_behavior {
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "${var.bucket}"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }
  }

  default_root_object = "index.html"

  custom_error_response {
    error_code         = 404
    response_code      = 200
    response_page_path = "/index.html"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn = "${var.acm_certificate_arn}"
    ssl_support_method  = "sni-only"
  }

  enabled         = true
  is_ipv6_enabled = true
  comment         = "${var.bucket}"
  aliases         = ["${var.domains}"]
  price_class     = "PriceClass_200"
}

resource "aws_cloudfront_origin_access_identity" "main" {
  comment = "${var.bucket}"
}

data "aws_route53_zone" "galpi" {
  name = "galpi.io."
}

resource "aws_route53_record" "root" {
  count   = "${length(var.domains)}"
  name    = "${var.domains[count.index]}"
  zone_id = "${data.aws_route53_zone.galpi.zone_id}"
  type    = "A"

  alias {
    name                   = "${aws_cloudfront_distribution.main.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.main.hosted_zone_id}"
    evaluate_target_health = true
  }
}
