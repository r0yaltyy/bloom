import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from random import randrange
from time import sleep

# Найти окно Telegram Desktop
telegram_window = gw.getWindowsWithTitle('screenshot_2548.jpg - 657x518 - 100% Gwenview')[0]

while True:
    # Получить координаты и размеры окна Telegram Desktop
    x, y, width, height = telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height

    # Сделать скриншот только из области окна Telegram Desktop
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Определить зеленые объекты на скриншоте
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([90, 255, 255])
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Найти контуры зеленых объектов
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        skip = randrange(1, 10) > 2
        if skip:
            area = cv2.contourArea(contour)
            if area > 100:  # Порог для минимальной площади объекта
                x, y, w, h = cv2.boundingRect(contour)
                center_x = x + w // 2
                center_y = y + h // 2
                pyautogui.click(center_x + randrange(-5, 5), center_y + randrange(-5, 5))  # Нажать на центр объекта

    if cv2.waitKey(1) & 0xFF == ord('q'):
        sleep(5)  # Приостановить выполнение на 5 секунд

cv2.destroyAllWindows()
