use piston_window::types::Color;
use piston_window::{Context, G2d};
use std::collections::LinkedList;

use draw::draw_block;

const SNAKE_COLOR: Color = [0.00, 0.80, 0.00, 1.00];

#[derive(Copy, Clone, PartialEq)]
pub enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT,
}

impl Direction {
    pub fn opposite(&self) -> Direction {
        match *self {
            Direction::UP => Direction::DOWN,
            Direction::DOWN => Direction::UP,
            Direction::LEFT => Direction::RIGHT,
            Direction::RIGHT => Direction::LEFT,
        }
    }
}

#[derive(Clone, Debug)]
struct Block {
    x: i32,
    y: i32,
}

pub struct Snake {
    direction: Direction,
    body: LinkedList<Block>,
    tail: Option<Block>,
}

impl Snake {
    pub fn new(x: i32, y: i32) -> Snake {
        let mut body: LinkedList<Block> = LinkedList::new();

        body.push_back(Block { x: x + 2, y });
        body.push_back(Block { x: x + 1, y });

        body.push_back(Block { x, y });

        Snake {
            direction: Direction::RIGHT,
            body,
            tail: None,
        }
    }

    pub fn draw(&self, ctx: &Context, g: &mut G2d) {
        for block in &self.body {
            draw_block(SNAKE_COLOR, block.x, block.y, ctx, g);
        }
    }

    pub fn head_position(&self) -> (i32, i32) {
        let head_block = self.body.front().unwrap();
        (head_block.x, head_block.y)
    }

    pub fn move_forward(&mut self, dir: Option<Direction>) {
        match dir {
            Some(d) => self.direction = d,
            None => {}
        }

        let (last_x, last_y): (i32, i32) = self.head_position();
        let new_block = match self.direction {
            Direction::UP => Block {
                x: last_x,
                y: last_y - 1,
            },
            Direction::DOWN => Block {
                x: last_x,
                y: last_y + 1,
            },
            Direction::LEFT => Block {
                x: last_x - 1,
                y: last_y,
            },
            Direction::RIGHT => Block {
                x: last_x + 1,
                y: last_y,
            },
        };

        self.body.push_front(new_block);
        let removed_block = self.body.pop_back().unwrap();
        self.tail = Some(removed_block);
    }

    pub fn head_direction(&self) -> Direction {
        self.direction
    }

    pub fn next_head(&mut self, dir: Option<Direction>) -> (i32, i32) {
        let (head_x, head_y): (i32, i32) = self.head_position();

        let mut moving_dir = self.direction;
        match dir {
            Some(d) => moving_dir = d,
            None => {}
        }

        match moving_dir {
            Direction::UP => (head_x, head_y - 1),
            Direction::DOWN => (head_x, head_y + 1),
            Direction::LEFT => (head_x - 1, head_y),
            Direction::RIGHT => (head_x + 1, head_y),
        }
    }

    pub fn restore_tail(&mut self) {
        let block = self.tail.clone().unwrap();
        self.body.push_back(block);
    }

    pub fn overlap_tail(&self, x: i32, y: i32) -> bool {
        let mut ch = 0;
        for block in &self.body {
            if x == block.x && y == block.y {
                return true;
            }

            ch += 1;
            if ch == self.body.len() - 1 {
                break;
            }
        }

        return false;
    }
}
