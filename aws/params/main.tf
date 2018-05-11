resource "aws_ssm_parameter" "client_id" {
  name  = "/galpi/${var.stage}/client_id"
  type  = "String"
  value = "${var.client_id}"
}

resource "aws_ssm_parameter" "client_secret" {
  name = "/galpi/${var.stage}/client_secret"
  type = "String"

  # Manage this value manually to keep it secret.
  value     = "<secret>"
  overwrite = false

  lifecycle {
    ignore_changes = ["value"]
  }
}

resource "aws_ssm_parameter" "secret_key" {
  name  = "/galpi/${var.stage}/secret_key"
  type  = "String"
  value = "${random_string.secret_key.result}"
}

resource "random_string" "secret_key" {
  length = 32
}

resource "aws_ssm_parameter" "bucket" {
  count = "${var.bucket != "" ? 1 : 0}"
  name  = "/galpi/${var.stage}/bucket"
  type  = "String"
  value = "${var.bucket}"
}

resource "aws_ssm_parameter" "distribution_id" {
  count = "${var.distribution_id != "" ? 1 : 0}"
  name  = "/galpi/${var.stage}/distribution_id"
  type  = "String"
  value = "${var.distribution_id}"
}
