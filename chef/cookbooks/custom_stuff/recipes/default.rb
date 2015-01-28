python_pip "web.py" do
  action :install
end

nodejs_npm "jquery" do
 action :install
end

cookbook_file "code.py" do
 path "/usr/local/bin/code.py"
 action :create
end

cookbook_file "rc.local" do
 path "/etc/rc.local"
 action :create
end

execute "rc.local" do
  command "/etc/rc.local"
end