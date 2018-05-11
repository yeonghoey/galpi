module "prod_client" {
  source              = "./client"
  bucket              = "galpi-prod"
  domains             = ["galpi.io", "www.galpi.io"]
  acm_certificate_arn = "${aws_acm_certificate.app.arn}"
}

module "prod_params" {
  source    = "./params"
  stage     = "prod"
  client_id = "e6fdc6f4954340579afe"
}
