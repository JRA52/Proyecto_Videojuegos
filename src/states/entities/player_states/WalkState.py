"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""

from gale.input_handler import InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.direction = direction
        self.entity.vx = settings.PLAYER_SPEED
        self.entity.vy = settings.PLAYER_SPEED
        
        if self.entity.direction == "left":
            self.entity.flipped = True
            self.entity.vx *= -1
            self.entity.vy = 0
        elif self.entity.direction == "right":
            self.entity.flipped = False
            self.entity.vy = 0
        elif self.entity.direction == "up": 
            self.entity.vx = 0
            self.entity.vy *= -1
        elif self.entity.direction == "down":
            self.entity.vx = 0
        self.entity.change_animation("walk")

    def update(self, dt: float) -> None:
        #if not self.entity.check_floor():
        #    self.entity.change_state("fall")

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
            elif input_data.released and self.entity.vx <= 0:
                self.entity.change_state("idle")

        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state("idle")

        elif input_id == "move_up":
            if input_data.pressed:
                self.entity.vy = -settings.PLAYER_SPEED
                ##self.entity.flipped = True
            elif input_data.released and self.entity.vy <= 0:
                self.entity.change_state("idle")
        
        elif input_id == "move_down":
            if input_data.pressed:
                self.entity.vy = settings.PLAYER_SPEED
                ##self.entity.flipped = True
            elif input_data.released and self.entity.vy >= 0:
                self.entity.change_state("idle")

        elif input_id == "jump" and input_data.pressed:
            self.entity.change_state("jump")
