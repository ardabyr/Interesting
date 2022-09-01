#!/bin/bash/

help(){
 echo "Укажите каталог, который хотите перекодировать bash lab21.sh [каталог]"
 echo "Вот пример правильного пользования скриптом: bash lab21.sh Загрузки"
}

kod(){
 enca -i "$file"
}

perekodirovka(){
 cd $katalog
 for fil in ls *.txt; do
  for file in $fil; do
      echo "Кодировка $file была:" && kod
    iconv -f kod -t UTF8 "$file" >tmp; mv tmp "$file"
      echo "Кодировка $file стала: " && kod
  done
 done
 echo "Done succesfully!"
}

katalog=$1

if [ "$katalog" == "" ]; then
 echo "Введите y, если хотите работать в домашней директории, n - если нет"
 read yn
 if [ "$yn" == "n" ]; then
  echo "Напишите: bash lab21.sh ?"
 elif [ "$yn" == "y" ]; then
  perekodirovka
 fi
elif [ "$katalog" == "?" ]; then
 help
else
 perekodirovka
fi

