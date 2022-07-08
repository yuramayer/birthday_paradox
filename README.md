# Парадокс Дней Рождения
> Математическое обоснование Парадокса дней рождения *(Birthday Paradox)* доступно [в Википедии в соответствующей статье](https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%BE%D0%BA%D1%81_%D0%B4%D0%BD%D0%B5%D0%B9_%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F)  


## О Разработке :wave:
Код наглядно демонстрирует реализацию Парадокса Дней Рождения - ситуацию, при которой в группе из **23 и более** человек **вероятность** как минимум одного **совпадения дней рождения превышает 50%**. 

Код был создан в рамках [Лаборатории Инноваций LegalTech](https://t.me/legaltechmsal) - образовательного проекта в области информационных технологий на базе МГЮА.  


## Зависимости :crocodile:
Для генерации случайных дней рождения используется библиотека [`Faker`](https://faker.readthedocs.io/en/master/).
Перед использованием кода её следует установить с помощью pip:
```python
pip install Faker
```


## Запуск :herb:
Программа включает несколько поэтапных шагов:
1. **Определение количества участников** в группе - иными словами, сколько дней рождения будут генерироваться
   - Код проведёт тест - выберет `N` случайных дней рождения и проверит, есть ли совпадение  

2. **Выбор количества симуляций** - сколько раз мы проверим случайные совпадения
   - Можно попробовать разные варианты - от 50 до 150.000 симуляций и убедиться на практике в [**Законе больших чисел**](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B8%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB)
   - Таймлайн настроен на каждые 10.000 симуляций:
   ```text
   0 simulations run...
   10000 simulations run...
   ...
   ```
   
3. **Подвод итогов** - сколько в итоге было зафиксировано совпадений
   - Код подсчитает как **общее количество совпадений**, так и итоговую **вероятность совпадения** дней рождений в группе. 
   - Чем больше количество симуляций, тем объективнее будет цифра вероятности - и тем ближе она будет к математическому результату 


## Попробовать! :sparkles:
Мы перенесли код на платформу Google.Colab, чтобы вы могли **запустить код прямо сейчас** - в вашем браузере! Для этого [**пройдите по ссылке, и последовательно включите ячейки с кодом**](https://colab.research.google.com/drive/1TYFjj66bVrWdPj2X9NN8g56nbyNbXCJX?usp=sharing) 

> Протестируйте разные группы на больших объёмах и убедитесь сами: **23 - волшебное число!** :wink:
