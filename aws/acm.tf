# Cloudfront requires ACM placed only in us-east-1
provider "aws" {
  alias  = "us-east-1"
  region = "us-east-1"
}

resource "aws_acm_certificate" "app" {
  provider = "aws.us-east-1"

  domain_name               = "galpi.io"
  subject_alternative_names = ["*.galpi.io"]
  validation_method         = "DNS"
}

resource "aws_acm_certificate" "api" {
  provider = "aws.us-east-1"

  domain_name               = "api.galpi.io"
  subject_alternative_names = ["*.api.galpi.io"]
  validation_method         = "DNS"
}
