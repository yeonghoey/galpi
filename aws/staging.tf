module "client_staging" {
  source              = "./client"
  bucket              = "galpi-staging"
  domains             = ["staging.galpi.io"]
  acm_certificate_arn = "${aws_acm_certificate.app.arn}"
}

module "params_staging" {
  source    = "./params"
  stage     = "staging"
  client_id = "fd7ab9a0164759ebf50f"
}
