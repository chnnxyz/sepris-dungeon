# The Island of Sepris, a DnD 5th Edition Puzzle Dungeon

## About
The Island of Sepris is a homebrew one-shot crafted by myself. While the plot is not mentioned here, this repo contains the base code for manipulating the dungeon.

## Dungeon Layout

The dungeon is laid out as a 3x3 grid with one or more empty spaces and behaves as a slider puzzle. Each room can be fully customized

The grid looks as follows:

```
    x -  0         1         2   
  y +---------+---------+---------+
  v |         |         |         |
  0 |         |         |         |
    |         |         |         | 
    +---------+---------+---------+
    |         |         |         |
  1 |         |         |         |
    |         |         |         | 
    +---------+---------+---------+
    |         |         |         |
  2 |         |         |         |
    |         |         |         | 
    +---------+---------+---------+
```

Empty spaces (of class `EmptySpace`) will be covered in `#`.

e.g.

```
    x -  0         1         2   
  y +---------+---------+---------+
  v |#########|         |         |
  0 |#########|         |         |
    |#########|         |         | 
    +---------+---------+---------+
    |         |         |         |
  1 |         |         |         |
    |         |         |         | 
    +---------+---------+---------+
    |         |         |         |
  2 |         |         |         |
    |         |         |         | 
    +---------+---------+---------+
```

Doors will show oneach available end by their position and single character keycode.

The party will be shown as `P` in a room. An example of both last points is as follows
```
+---------+---------+---------+
|   ---   |#########|#########|
|         |#########|#########|
|   ---   |#########|#########| 
+---------+---------+---------+
|         |   ---   |         |
|       | | |     | | |     | |
|   ---   |   ---   |         | 
+---------+---------+---------+
|#########|   xxx   |         |
|#########|    P  | | |       |
|#########|         |   ---   | 
+---------+---------+---------+
```

## How to run

- Step 1: Clone Repo
- Step 2: Edit `src/__main__.py` to build rooms accordingly
- Step 3: run `python -m src`

### Dependencies

None lol

## Dungeon Operations

### Gravity
Gravity (selected by `g`) will move everything on a direction until colission. Available directions are `n`, `e`, `s` and `w`.

Example:
```
+---------+---------+---------+
|   ---   |#########|#########|
|         |#########|#########|
|   ---   |#########|#########| 
+---------+---------+---------+
|         |   ---   |         |
|       | | |     | | |     | |
|   ---   |   ---   |         | 
+---------+---------+---------+
|#########|   xxx   |         |
|#########|    P  | | |       |
|#########|         |   ---   | 
+---------+---------+---------+

select action: g
select gravity magic direction: w

+---------+---------+---------+
|   ---   |#########|#########|
|         |#########|#########|
|   ---   |#########|#########| 
+---------+---------+---------+
|         |   ---   |         |
|       | | |     | | |     | |
|   ---   |   ---   |         | 
+---------+---------+---------+
|   xxx   |         |#########|
|    P  | | |       |#########|
|         |   ---   |#########| 
+---------+---------+---------+
```

### Move Room

Move a selected room on x, y coordinates in a direction, selected with `m`.
Available directions are `n`, `e`, `s` and `w`.

```
+---------+---------+---------+
|   ---   |#########|#########|
|         |#########|#########|
|   ---   |#########|#########| 
+---------+---------+---------+
|         |   ---   |         |
|       | | |     | | |     | |
|   ---   |   ---   |         | 
+---------+---------+---------+
|   xxx   |         |#########|
|    P  | | |       |#########|
|         |   ---   |#########| 
+---------+---------+---------+

Action: m
select room (format: x y): 0 0
Room movement direction: e
party is at x=0, y=2
+---------+---------+---------+
|#########|   ---   |#########|
|#########|         |#########|
|#########|   ---   |#########| 
+---------+---------+---------+
|         |   ---   |         |
|       | | |     | | |     | |
|   ---   |   ---   |         | 
+---------+---------+---------+
|   xxx   |         |#########|
|    P  | | |       |#########|
|         |   ---   |#########| 
+---------+---------+---------+
```

### Move Party
Command is `e`, for Enter and Exit. provide a direction. These are `n`, `s`, `e`, `w`

This method currently has no colission or door detection, since this software is just DM help

## Play with it

Buiold some rooms, add random enemy spawns, have fun. you only need to modify `src/__main__.py`