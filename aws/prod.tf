module "params_prod" {
  source    = "./params"
  stage     = "prod"
  client_id = "e6fdc6f4954340579afe"
}

module "client_prod" {
  source              = "./client"
  bucket              = "galpi-prod"
  domains             = ["galpi.io", "www.galpi.io"]
  acm_certificate_arn = "${aws_acm_certificate.app.arn}"
}
