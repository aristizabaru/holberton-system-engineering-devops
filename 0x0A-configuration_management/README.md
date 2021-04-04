# 0x0A Configuration management

## About

This is an educational project to explore several concepts about DevOps and software configuration management with technologies as Puppet.

**INTRO VIDEO**  
[Intro to configuration management](https://www.youtube.com/watch?v=ogYLFyp68cI&feature=youtu.be)

## Topics

-  What is configuration management
-  Which are the most popular configuration management thecnologies
-  What is Puppet
-  How does Puppet works

## Requirements

-  Ubuntu 14.04 LTS
-  Puppet (version 5.4.x)
-  puppet-lint (version 2.1.1)

**Install puppet**

```
$ sudo apt-get install puppet
```

**Install puppet-lint**

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Read or watch

-  [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
-  [Puppet resource type: file](https://puppet.com/docs/puppet/3.8/types/file.html)_(check “Resource types” for all manifest types in the left menu)_
-  [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## File Descriptions

This project is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### 0. Create a file

**[0-create_a_file.pp](0-create_a_file.pp)**

Using Puppet, create a file in `/tmp`.

Requirements:

- File path is `/tmp/holberton`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

Example:

```
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.1.1
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[holberton]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/holberton
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/holberton
root@6712bef7a528:~# cat /tmp/holberton
I love Puppetroot@6712bef7a528:~#
```
### 1. Install a package

**[1-install_a_package.pp](1-install_a_package.pp)**

Using Puppet, install `puppet-lint`.

Requirements:

- Install `puppet-lint`
- Version must be `2.1.1`

Example:

```
root@d391259bf577:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
Notice: Finished catalog run in 2.83 seconds
root@d391259bf577:/# gem list

*** LOCAL GEMS ***

puppet-lint (2.1.1)
root@d391259bf577:/#
```

### 2. Execute a command

**[2-execute_a_command.pp](2-execute_a_command.pp)**

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`

Example:

Terminal #0 - starting my process
```
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

Terminal #1 - executing my manifest
```
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
```

Terminal #0 - process has been terminated
```
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```