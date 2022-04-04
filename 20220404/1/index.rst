.. No project documentation master file, created by
   sphinx-quickstart on Mon Apr  4 12:37:19 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to No project's documentation!
======================================

.. code-block:: python

   class Player:
      """Класс игрока - юзера приложения."""
      coords = []

      def __init__(self, coords=[0, 0]):
         self.coords = coords


   class Monster:
      """Класс монстра, блуждающего в поисках нуба."""
      name = 0
      hp = 0

      def __init__(self, name, hp=15):
         self.name = name
         self.hp = hp

	
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Суть проекта:
Проверять письма по курсу `сетей`_. И в автоматическом режиме показывать оперативную статистику на `сайте`_

Участники:

   #. Арефьев Вениамин Андреевич, группа 321, nick: Veniamin-Arefev
   #. Оконишников Арий Ариевич, группа 321, nick: Uberariy
   #. Стамплевский Дмитрий Максимович, группа 321, nick: stamplevskiyd

Ссылка на публичный репозиторий: `https://github.com/Veniamin-Arefev/NetJudge`_

Внимание, море:

|море|

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _https://github.com/Veniamin-Arefev/NetJudge: https://github.com/Veniamin-Arefev/NetJudge
.. _сетей: https://uneex.ru/LecturesCMC/LinuxNetwork2022
.. _сайте: https://uneex.veniamin.space/
.. |море| image:: _static/sea.jpg
