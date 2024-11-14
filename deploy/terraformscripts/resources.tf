resource "aws_instance" "ec2_os1" {
  ami = ""
  instance = "t2.micro"
  key_name = 
  subnet_id = ""
  tags = {
Name = "test-ec2"
    }

  
