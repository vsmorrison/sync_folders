# Синхронизация каталогов

## Краткое описание проекта

Скрипт синхронизирует каталог-источник с каталогом-репликой. Синхронизация происходит с указанной пользователем частотой. 

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3) для установки зависимостей:

```
pip install -r requirements.txt
```

## Как запустить

Для запуска проекта в консоли необходимо выполнить команду:

```
python3 main.py source replica sync_interval log_path 
```
```source``` - путь к каталогу-источнику

```replica``` - путь к каталогу-реплике

```sync_interval``` - интервал синхронизации каталогов

```log_path``` - путь к каталогу с лог-файлом

## Результаты выполнения

Процесс выполнения скрипта выводится в терминал и записывается в файл, путь к которому указывает пользователь - 
{path}/Sync report [time].log