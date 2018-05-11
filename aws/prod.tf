module "prod_appdist" {
  source              = "./appdist"
  bucket              = "galpi-prod"
  domains             = ["galpi.io", "www.galpi.io"]
  acm_certificate_arn = "${aws_acm_certificate.app.arn}"
}

module "prod_params" {
  source          = "./params"
  stage           = "prod"
  client_id       = "e6fdc6f4954340579afe"
  bucket          = "${module.prod_appdist.bucket}"
  distribution_id = "${module.prod_appdist.distribution_id}"
}
