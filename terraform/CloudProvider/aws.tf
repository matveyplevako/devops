terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = "us-east-1"
  profile    = "default"
}

resource "aws_instance" "app" {
  ami           = "ami-0b9064170e32bde34"
  instance_type = "t2.micro"

  tags = {
    Name = "Moscow Time Server"
  }
}
