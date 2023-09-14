Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  
  config.vm.network "forwarded_port", guest: 5000, host: 5003

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install Flask
  SHELL
  
  config.vm.provision "file", source: "./app.py", destination: "~/app.py"
  config.vm.provision "file", source: "./templates", destination: "~/templates"
  config.vm.provision "file", source: "./static", destination: "~/static"

  config.vm.provision "shell", inline: <<-SHELL
    nohup python3 ~/app.py &
  SHELL
end
