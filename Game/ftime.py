import pygame
import numpy as np


class Timecount:

    def __init__(self, window, res_w, res_h, Second, Minute, Hour, Day):
        self.window = window
        self.res_w = res_w
        self.res_h = res_h
        self.Second = Second
        self.Minute = Minute
        self.Hour = Hour
        self.Day = Day
        self.Mil = 0
        self.Black = (150, 150, 150)
        self.Darkness = (115, 118, 83)

        self.logs = 3
        self.matches = 10
        self.lantern = 0

    def update_time(self):
        self.Mil += 1
        if self.Mil == 10:
            self.Second += 1
            self.Mil = 0
        if self.Second == 60:
            self.Minute += 1
            self.Second = 0
        if self.Minute == 60:
            self.Hour += 1
            self.Minute = 0
        if self.Hour == 12:
            self.Day += 1
            self.Hour = 0

        self.Font = pygame.font.SysFont("Trebuchet MS", 25)
        DayFont = self.Font.render(
            "Day:{0:03}".format(self.Day), 1, self.Black
        )  # zero-pad day to 3 digits
        self.DayFontR = DayFont.get_rect()
        self.DayFontR.center = (100, 20)
        # Hour
        HourFont = self.Font.render(
            "Hour:{0:02}".format(self.Hour), 1, self.Black
        )  # zero-pad hours to 2 digits
        self.HourFontR = HourFont.get_rect()
        self.HourFontR.center = (1120, 20)
        # Minute
        MinuteFont = self.Font.render(
            "Minute:{0:02}".format(self.Minute), 1, self.Black
        )  # zero-pad minutes to 2 digits
        self.MinuteFontR = MinuteFont.get_rect()
        self.MinuteFontR.center = (1165, 20)

        SecondFont = self.Font.render(
            "Second:{0:02}".format(self.Second), 1, self.Black
        )  # zero-pad Seconds to 2 digits
        self.SecondFontR = SecondFont.get_rect()
        self.SecondFontR.center = (1200, 20)

        logFont = self.Font.render("Log:{0}".format(self.logs), 1, self.Black)
        self.logFontR = logFont.get_rect()
        self.logFontR.center = (200, 20)

        matchboxFont = self.Font.render("MatchBox:{0}".format(self.logs), 1,
                                        self.Black)
        self.matchboxR = matchboxFont.get_rect()
        self.matchboxR.center = (305, 20)

        lanternFont = self.Font.render("lantern:{0}".format(self.lantern), 1,
                                       self.Black)
        self.lanternR = lanternFont.get_rect()
        self.lanternR.center = (350, 20)

    def update_overlay(self):
        SecondFont = self.Font.render("{0:02}".format(self.Second), 1, self.Black)
        self.window.blit(SecondFont, self.SecondFontR)
        MinuteFont = self.Font.render("{0:02}:".format(self.Minute), 1, self.Black)
        self.window.blit(MinuteFont, self.MinuteFontR)
        HourFont = self.Font.render("{0:02}:".format(self.Hour), 1, self.Black)
        self.window.blit(HourFont, self.HourFontR)
        DayFont = self.Font.render("Day:{0:01}".format(self.Day), 1, self.Black)
        self.window.blit(DayFont, self.DayFontR)
        logFont = self.Font.render("{0:01}".format(self.logs), 1, self.Black)
        self.window.blit(logFont, self.logFontR)
        matchboxFont = self.Font.render("{0:01}".format(self.matches), 1, self.Black)
        self.window.blit(matchboxFont, self.matchboxR)
        lanternFont = self.Font.render("{0:01}".format(self.lantern), 1, self.Black)
        self.window.blit(lanternFont, self.lanternR)

    def get_time(self):
        return [self.Mil, self.Second, self.Minute]

    def add_item(self, var):
        if var == "Log":
            self.logs += 1
        elif var == "Matchbox":
            self.matches += 5
        elif var == 'Oilcan':
            self.lantern += 3

    def remove_item(self, var):
        if var == "Log":
            self.logs -= 1
        elif var == "match":
            self.matches -= 1
        elif var == "Oilcan":
            self.lantern -= 1

    def get_logs(self):
        return self.logs

    def get_matches(self):
        return self.matches

    def get_oil(self):
        return self.lantern
