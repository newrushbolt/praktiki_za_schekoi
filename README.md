# StyleConvention

В этом репо живут наши соглашения о работе с различными инструментами.  
Правки применяются только через Merge Request с апрувом(посредством емодзи) от большинства сотрудников.  
За корректностью разметки и текстов приглядыют автотесты.

## Ручной запуск тестов

### markdownlint

`docker run -it -v "$PWD:/code" pipelinecomponents/markdownlint:5d96213 mdl -s md.rb -w .`

## Генерация заголовков

`python contents.py < Ansible.md`