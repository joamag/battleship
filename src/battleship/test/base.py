#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import battleship


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.game = battleship.Battleship(allocate=False)

    def tearDown(self):
        pass

    def test_initial(self):
        self.assertEqual(self.game.pending, 0)

    def test_allocate(self):
        self.game.allocate()
        self.assertEqual(self.game.pending, 13)

        self.game.allocate()
        self.assertEqual(self.game.pending, 26)

        self.game.destroy()
        self.assertEqual(self.game.pending, 0)

    def test_shoot(self):
        self.assertNotEqual(self.game.shoot("a1"), None)