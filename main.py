from pydantic import BaseModel
from typing import List, Literal, Annotated
import random

# Define possible options
EQUIPMENT_OPTIONS = [
    "None", "Dumbbells", "Barbells", "Resistance Bands", "Kettlebells", "Full Gym"
]
GOAL_OPTIONS = [
    "Lose Weight", "Build Muscle", "Increase Endurance & Athleticism", "General Fitness"
]

class WorkoutRequest(BaseModel):
    days_per_week: Annotated[int, (1, 7)]  # Accepts int, must be between 1 and 7
    equipment: List[Literal[
        "None", "Dumbbells", "Barbells", "Resistance Bands", "Kettlebells", "Full Gym"
    ]]
    goal: Literal[
        "Lose Weight", "Build Muscle", "Increase Endurance & Athleticism", "General Fitness"
    ]

# Example exercise dictionary with subgroups for 'back'
EXERCISES = {
    "back": {
        "upper": {
            "None": [
                {"name": "Reverse Snow Angels", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Prone Y-T-I Raises", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Back Widows", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Superman Pulls", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Doorway Rows (Towel Row)", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Rows", "sets": 4, "reps": 10, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Rows", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Face Pulls", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell High Pulls", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Lat Pulldown", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Seated Row", "sets": 4, "reps": 10, "rest_seconds": 75}
            ]
        },
        "lower": {
            "None": [
                {"name": "Supermans", "sets": 3, "reps": 20, "rest_seconds": 30},
                {"name": "Alternating Superman", "sets": 3, "reps": 16, "rest_seconds": 30},
                {"name": "Reverse Hyperextensions (on floor)", "sets": 3, "reps": 15, "rest_seconds": 30},
                {"name": "Glute Bridge March", "sets": 3, "reps": 16, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Deadlifts", "sets": 4, "reps": 12, "rest_seconds": 90}
            ],
            "Barbells": [
                {"name": "Barbell Deadlifts", "sets": 4, "reps": 6, "rest_seconds": 120}
            ],
            "Resistance Bands": [
                {"name": "Band Good Mornings", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Swings", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Back Extension", "sets": 3, "reps": 15, "rest_seconds": 60}
            ]
        }
    },
    "chest": {
        "upper": {
            "None": [
                {"name": "Incline Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Incline Dumbbell Press", "sets": 4, "reps": 10, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Incline Barbell Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press (Incline)", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Incline Kettlebell Press", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Incline Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ]
        },
        "lower": {
            "None": [
                {"name": "Decline Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Decline Dumbbell Press", "sets": 4, "reps": 10, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Decline Barbell Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press (Decline)", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Decline Kettlebell Press", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Decline Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ]
        },
        "mid": {
            "None": [
                {"name": "Push-ups", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Bench Press", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Dumbbell Flyes", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Dumbbell Floor Press", "sets": 3, "reps": 10, "rest_seconds": 60},
                {"name": "Dumbbell Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Dumbbell Pullover", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90},
                {"name": "Barbell Close-Grip Bench Press", "sets": 3, "reps": 10, "rest_seconds": 75},
                {"name": "Barbell Floor Press", "sets": 3, "reps": 8, "rest_seconds": 75},
                {"name": "Barbell Pin Press", "sets": 3, "reps": 8, "rest_seconds": 75}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Band Flyes", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Band Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Band Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Floor Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Kettlebell Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Kettlebell Flyes", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Chest Press Machine", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90},
                {"name": "Pec Deck Machine", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Cable Flyes", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Incline Chest Press Machine", "sets": 3, "reps": 10, "rest_seconds": 75}
            ]
        }
    },
    "legs": {
        "quads": {
            "None": [
                {"name": "Bodyweight Squats", "sets": 4, "reps": 15, "rest_seconds": 60},
                {"name": "Split Squats", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Wall Sit", "sets": 3, "reps": 45, "rest_seconds": 45},  # seconds hold
                {"name": "Step-Ups (on chair/step)", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Reverse Lunges", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Lunges", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Squats", "sets": 4, "reps": 8, "rest_seconds": 120}
            ],
            "Resistance Bands": [
                {"name": "Band Squats", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Goblet Squats", "sets": 4, "reps": 12, "rest_seconds": 75}
            ],
            "Full Gym": [
                {"name": "Leg Press", "sets": 4, "reps": 10, "rest_seconds": 90}
            ]
        },
        "hamstrings": {
            "None": [
                {"name": "Glute Bridge", "sets": 3, "reps": 20, "rest_seconds": 45},
                {"name": "Single-Leg Glute Bridge", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Sliding Leg Curl (on towel)", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Hip Thrust (bodyweight)", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Romanian Deadlift", "sets": 4, "reps": 12, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Barbell Romanian Deadlift", "sets": 4, "reps": 10, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Leg Curl", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Swings", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Leg Curl Machine", "sets": 4, "reps": 12, "rest_seconds": 75}
            ]
        },
        "glutes": {
            "None": [
                {"name": "Glute Bridge March", "sets": 3, "reps": 16, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Hip Thrust", "sets": 4, "reps": 12, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Hip Thrust", "sets": 4, "reps": 10, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Banded Glute Bridge", "sets": 4, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Hip Thrust", "sets": 4, "reps": 12, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Cable Kickback", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        },
        "calves": {
            "None": [
                {"name": "Standing Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45},
                {"name": "Single-Leg Calf Raise", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Seated Calf Raise (bodyweight)", "sets": 3, "reps": 20, "rest_seconds": 45},
                {"name": "Calf Raise Hold (isometric)", "sets": 3, "reps": 30, "rest_seconds": 30}  # seconds hold
            ],
            "Dumbbells": [
                {"name": "Dumbbell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Calf Raise Machine", "sets": 4, "reps": 20, "rest_seconds": 60}
            ]
        }
    },
    "core": {
        "upper": {
            "None": [
                {"name": "Crunches", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Weighted Crunches", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Barbells": [],
            "Resistance Bands": [
                {"name": "Band Crunches", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Kettlebells": [],
            "Full Gym": [
                {"name": "Cable Crunch", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        },
        "lower": {
            "None": [
                {"name": "Leg Raises", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Weighted Leg Raises", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [],
            "Resistance Bands": [
                {"name": "Band Leg Raises", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Kettlebells": [],
            "Full Gym": [
                {"name": "Hanging Leg Raise", "sets": 3, "reps": 10, "rest_seconds": 60}
            ]
        },
        "obliques": {
            "None": [
                {"name": "Russian Twists", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Side Bend", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Barbells": [
                {"name": "Landmine Twists", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Woodchoppers", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Russian Twists", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Full Gym": [
                {"name": "Cable Woodchopper", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        }
    },
    "arms": {
        "biceps": {
            "None": [
                {"name": "Isometric Curl Hold", "sets": 3, "reps": 30, "rest_seconds": 30}  # seconds hold
            ],
            "Dumbbells": [
                {"name": "Dumbbell Bicep Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Curl", "sets": 4, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Curl", "sets": 4, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Cable Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ]
        },
        "triceps": {
            "None": [
                {"name": "Diamond Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Tricep Extension", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Skullcrusher", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Tricep Extension", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Tricep Extension", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Cable Tricep Pushdown", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        },
        "forearms": {
            "None": [
                {"name": "Reverse Push-ups", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Barbells": [
                {"name": "Barbell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Resistance Bands": [
                {"name": "Band Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Full Gym": [
                {"name": "Forearm Machine", "sets": 3, "reps": 20, "rest_seconds": 30}
            ]
        }
    },
    "shoulders": {
        "front": {
            "None": [
                {"name": "Pike Push-ups", "sets": 3, "reps": 10, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Front Raise", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Shoulder Press Machine", "sets": 4, "reps": 10, "rest_seconds": 75}
            ]
        },
        "side": {
            "None": [
                {"name": "Plank to Push-up", "sets": 3, "reps": 10, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Lateral Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Upright Row", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Lateral Raise", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Lateral Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Lateral Raise Machine", "sets": 3, "reps": 12, "rest_seconds": 45}
            ]
        },
        "rear": {
            "None": [
                {"name": "Reverse Snow Angels", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Reverse Fly", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Reverse Pec Deck", "sets": 3, "reps": 12, "rest_seconds": 45}
            ]
        }
    }
}

# Cardio and plyometric exercises for each equipment type
CARDIO_PLYO_EXERCISES = {
    "None": [
        {"name": "Jumping Jacks", "time_seconds": 45, "rest_seconds": 15},
        {"name": "Mountain Climbers", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Burpees", "time_seconds": 30, "rest_seconds": 30},
        {"name": "High Knees", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Bodyweight Lateral Hops", "time_seconds": 30, "rest_seconds": 20},
        {"name": "Skater Jumps", "time_seconds": 30, "rest_seconds": 20},
        {"name": "Plank Jacks", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Tuck Jumps", "time_seconds": 20, "rest_seconds": 30},
        {"name": "Shadow Boxing", "time_seconds": 60, "rest_seconds": 15},
        {"name": "Stair Runs", "time_seconds": 60, "rest_seconds": 30},
    ],
    "Dumbbells": [
        {"name": "Dumbbell Thrusters", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Snatch", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Swings", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Lateral Shuffle Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Barbells": [
        {"name": "Barbell Complex (Deadlift, Row, Clean, Press)", "time_seconds": 60, "rest_seconds": 60},
        {"name": "Barbell Push Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Resistance Bands": [
        {"name": "Band Sprints (anchor band and run in place)", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Band Jump Squats", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Band High Knees", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Kettlebells": [
        {"name": "Kettlebell Swings", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Kettlebell Snatch", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Kettlebell Clean and Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Full Gym": [
        {"name": "Treadmill Run", "time_seconds": 300, "rest_seconds": 60},
        {"name": "Rowing Machine", "time_seconds": 180, "rest_seconds": 60},
        {"name": "Battle Ropes", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Box Jumps", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Assault Bike", "time_seconds": 120, "rest_seconds": 60},
    ]
}

RUNNING_WORKOUTS = [
    {
        "name": "8 x 800m Intervals",
        "description": "8 sets of 800m run at fast pace, 2 min rest between sets",
        "sets": 8,
        "distance_m": 800,
        "rest_seconds": 120
    },
    {
        "name": "5K Tempo Run",
        "description": "5km run at comfortably hard pace",
        "sets": 1,
        "distance_m": 5000,
        "rest_seconds": 0
    },
    {
        "name": "Long Run",
        "description": "Steady pace long run (8-12km)",
        "sets": 1,
        "distance_m": 10000,
        "rest_seconds": 0
    },
    {
        "name": "Fartlek Run",
        "description": "45 min run with random surges (1-2 min fast, 2-3 min easy)",
        "sets": 1,
        "time_minutes": 45,
        "rest_seconds": 0
    },
    {
        "name": "Hill Sprints",
        "description": "10 x 30s hill sprints, walk down for rest",
        "sets": 10,
        "time_seconds": 30,
        "rest_seconds": 90
    },
    {
        "name": "Progression Run",
        "description": "6km run, start easy and finish fast",
        "sets": 1,
        "distance_m": 6000,
        "rest_seconds": 0
    }
]

FAT_BURNING_EXERCISES = {
    "None": [
        {"name": "Burpees", "time_seconds": 40, "rest_seconds": 20, "description": "Full-body explosive movement, high calorie burn."},
        {"name": "Mountain Climbers", "time_seconds": 45, "rest_seconds": 15, "description": "Fast-paced core and cardio exercise."},
        {"name": "Jump Squats", "time_seconds": 30, "rest_seconds": 30, "description": "Legs and glutes, plyometric power."},
        {"name": "High Knees", "time_seconds": 40, "rest_seconds": 20, "description": "Cardio, core, and hip flexors."},
        {"name": "Plank Jacks", "time_seconds": 40, "rest_seconds": 20, "description": "Core and shoulders, fast-paced."},
        {"name": "Skater Hops", "time_seconds": 30, "rest_seconds": 30, "description": "Lateral movement, legs and cardio."},
        {"name": "Tuck Jumps", "time_seconds": 20, "rest_seconds": 40, "description": "Explosive plyometric jump."},
        {"name": "Shadow Boxing", "time_seconds": 60, "rest_seconds": 20, "description": "Upper body, fast-paced cardio."},
        {"name": "Lunge Jumps", "time_seconds": 30, "rest_seconds": 30, "description": "Legs, glutes, and cardio."},
        {"name": "Push-up to Knee Tuck", "time_seconds": 30, "rest_seconds": 30, "description": "Upper body and core, high intensity."},
    ],
    "Dumbbells": [
        {"name": "Dumbbell Thrusters", "time_seconds": 30, "rest_seconds": 30, "description": "Squat to press, full-body HIIT."},
        {"name": "Dumbbell Snatch", "time_seconds": 30, "rest_seconds": 30, "description": "Explosive full-body movement."},
        {"name": "Dumbbell Swings", "time_seconds": 30, "rest_seconds": 30, "description": "Hip hinge, glutes, and cardio."},
        {"name": "Dumbbell Lateral Shuffle Press", "time_seconds": 30, "rest_seconds": 30, "description": "Lateral movement, upper body."},
    ],
    "Kettlebells": [
        {"name": "Kettlebell Swings", "time_seconds": 30, "rest_seconds": 30, "description": "Explosive hip drive, high calorie burn."},
        {"name": "Kettlebell Snatch", "time_seconds": 30, "rest_seconds": 30, "description": "Full-body HIIT."},
        {"name": "Kettlebell Clean and Press", "time_seconds": 30, "rest_seconds": 30, "description": "Total body, metabolic conditioning."},
    ],
    "Full Gym": [
        {"name": "Battle Ropes", "time_seconds": 30, "rest_seconds": 30, "description": "Upper body, core, and cardio."},
        {"name": "Box Jumps", "time_seconds": 30, "rest_seconds": 30, "description": "Explosive plyometric, legs."},
        {"name": "Assault Bike", "time_seconds": 60, "rest_seconds": 30, "description": "Full-body, high-intensity cardio."},
        {"name": "Treadmill Sprints", "time_seconds": 30, "rest_seconds": 30, "description": "Max effort running intervals."},
        {"name": "Rowing Machine Sprints", "time_seconds": 45, "rest_seconds": 30, "description": "Full-body, high calorie burn."},
    ]
}

def get_exercises_for_muscle(muscle, user_equipment, min_per_muscle=2, force_all_subgroups=False):
    # If user has Full Gym, only use Full Gym exercises
    if "Full Gym" in user_equipment:
        user_equipment = ["Full Gym"]
    muscle_dict = EXERCISES.get(muscle, {})
    day_exercises = []
    for subgroup, eq_dict in muscle_dict.items():
        possible = []
        for eq in user_equipment:
            possible += eq_dict.get(eq, [])
        if possible:
            n = min_per_muscle
            if force_all_subgroups:
                n = max(1, min_per_muscle)  # Always at least 1 per subgroup
            n = min(n, len(possible))
            day_exercises.extend(random.sample(possible, k=n))
    return day_exercises

# Define splits for 'Build Muscle' goal
MUSCLE_SPLITS = {
    1: ["full body"],
    2: ["upper body", "lower body"],
    3: ["push", "pull", "legs"],
    4: ["upper body", "lower body", "push", "pull"],
    5: ["push", "pull", "legs", "upper body", "lower body"],
    6: ["push", "pull", "legs", "push", "pull", "legs"],
    7: ["push", "pull", "legs", "upper body", "lower body", "full body", "active recovery"]
}

# Map splits to muscle groups
SPLIT_MUSCLES = {
    "push": ["chest", "shoulders", "triceps"],
    "pull": ["back", "biceps", "forearms"],
    "legs": ["legs", "core"],
    "upper body": ["chest", "back", "shoulders", "biceps", "triceps", "forearms"],
    "lower body": ["legs", "core"],
    "full body": ["chest", "back", "shoulders", "biceps", "triceps", "forearms", "legs", "core"],
    "active recovery": []  # Could be stretching, yoga, etc.
}

# Helper for active recovery
ACTIVE_RECOVERY = [
    "Child's Pose",
    "Downward Dog",
    "Cat-Cow Stretch",
    "Seated Forward Fold",
    "Cobra Pose",
    "Thread the Needle",
    "Supine Twist",
    "Butterfly Stretch",
    "Pigeon Pose",
    "Foam Rolling",
    "Walking",
]

def generate_workout(days_per_week, equipment, goal):
    # If user has Full Gym, only use Full Gym exercises
    if "Full Gym" in equipment:
        equipment = ["Full Gym"]
    workout_plan = []
    min_exercises_per_day = 5
    if goal == "Build Muscle":
        splits = MUSCLE_SPLITS.get(days_per_week, ["full body"])
        for day, split in enumerate(splits):
            if split == "active recovery":
                exercises = [
                    {"name": ex, "time_seconds": 60, "rest_seconds": 15}
                    for ex in random.sample(ACTIVE_RECOVERY, k=min(2, len(ACTIVE_RECOVERY)))
                ]
                workout_plan.append({
                    "day": day + 1,
                    "split": split.title(),
                    "exercises": exercises
                })
                continue
            muscles = SPLIT_MUSCLES[split]
            day_exercises = []
            # Special handling for legs/lower body days
            if split in ["legs", "lower body"]:
                # Add one from each legs subgroup
                for leg_part in ["quads", "hamstrings", "glutes", "calves"]:
                    leg_exs = []
                    for eq in equipment:
                        leg_exs += EXERCISES["legs"].get(leg_part, {}).get(eq, [])
                    if leg_exs:
                        day_exercises.append(random.choice(leg_exs))
                # Add 1-2 core exercises (from random subgroups)
                core_subgroups = list(EXERCISES["core"].keys())
                chosen_core = random.sample(core_subgroups, k=min(2, len(core_subgroups)))
                for subgroup in chosen_core:
                    core_exs = []
                    for eq in equipment:
                        core_exs += EXERCISES["core"].get(subgroup, {}).get(eq, [])
                    if core_exs:
                        day_exercises.append(random.choice(core_exs))
                # Change label for split
                split_label = "Legs & Core" if split == "legs" else "Lower Body & Core"
            else:
                force_all_subgroups = split in ["pull"]
                split_label = split.title()
                for muscle in muscles:
                    min_per = 2 if not force_all_subgroups else 1
                    day_exercises.extend(get_exercises_for_muscle(muscle, equipment, min_per_muscle=min_per, force_all_subgroups=force_all_subgroups))
            # Remove duplicates by exercise name
            seen = set()
            unique_exercises = []
            for ex in day_exercises:
                if ex['name'] not in seen:
                    unique_exercises.append(ex)
                    seen.add(ex['name'])
            # If less than min_exercises_per_day, fill with more from all muscles
            if len(unique_exercises) < min_exercises_per_day:
                all_possible = []
                for muscle in muscles:
                    all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=2, force_all_subgroups=(split in ["pull"]))
                random.shuffle(all_possible)
                for ex in all_possible:
                    if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                        unique_exercises.append(ex)
                        seen.add(ex['name'])
            workout_plan.append({
                "day": day + 1,
                "split": split_label,
                "exercises": unique_exercises[:min_exercises_per_day],
                "rest_between_exercises_seconds": 90
            })
    elif goal == "General Fitness":
        splits = MUSCLE_SPLITS.get(days_per_week, ["full body"])
        num_days = days_per_week
        min_exercises_per_day = 5
        if num_days <= 4:
            # Only 1 cardio/plyometric day, rest are weightlifting
            cardio_day = random.randint(0, num_days - 1)
            for day in range(num_days):
                if day == cardio_day:
                    cardio_exercises = []
                    for eq in equipment:
                        cardio_exercises += random.sample(
                            CARDIO_PLYO_EXERCISES.get(eq, []),
                            k=min(4, len(CARDIO_PLYO_EXERCISES.get(eq, [])))
                        )
                    if not cardio_exercises:
                        cardio_exercises = random.sample(CARDIO_PLYO_EXERCISES["None"], k=4)
                    # Add sets=3 to each cardio/plyo exercise
                    for ex in cardio_exercises:
                        ex["sets"] = 3
                    workout_plan.append({
                        "day": day + 1,
                        "split": "Cardio/Plyometric",
                        "exercises": cardio_exercises,
                        "rest_between_exercises_seconds": 45
                    })
                else:
                    split = splits[day % len(splits)]
                    muscles = SPLIT_MUSCLES[split]
                    day_exercises = []
                    if split in ["legs", "lower body"]:
                        for leg_part in ["quads", "hamstrings", "glutes", "calves"]:
                            leg_exs = []
                            for eq in equipment:
                                leg_exs += EXERCISES["legs"].get(leg_part, {}).get(eq, [])
                        if leg_exs:
                            day_exercises.append(random.choice(leg_exs))
                        # Add 1 core exercise (from random subgroup)
                        core_subgroups = list(EXERCISES["core"].keys())
                        chosen_core = random.sample(core_subgroups, k=min(1, len(core_subgroups)))
                        for subgroup in chosen_core:
                            core_exs = []
                            for eq in equipment:
                                core_exs += EXERCISES["core"].get(subgroup, {}).get(eq, [])
                            if core_exs:
                                day_exercises.append(random.choice(core_exs))
                        split_label = "Legs & Core" if split == "legs" else "Lower Body & Core"
                    else:
                        split_label = split.title()
                        for muscle in muscles:
                            day_exercises.extend(get_exercises_for_muscle(muscle, equipment, min_per_muscle=2))
                    # Remove duplicates by exercise name
                    seen = set()
                    unique_exercises = []
                    for ex in day_exercises:
                        if ex['name'] not in seen:
                            unique_exercises.append(ex)
                            seen.add(ex['name'])
                    # If less than min_exercises_per_day, fill with more from all muscles
                    if len(unique_exercises) < min_exercises_per_day:
                        all_possible = []
                        for muscle in muscles:
                            all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=2)
                        random.shuffle(all_possible)
                        for ex in all_possible:
                            if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                                unique_exercises.append(ex)
                                seen.add(ex['name'])
                    workout_plan.append({
                        "day": day + 1,
                        "split": split_label,
                        "exercises": unique_exercises[:min_exercises_per_day],
                        "rest_between_exercises_seconds": 90
                    })
        else:
            # More days than splits, repeat some splits
            for day in range(num_days):
                split = splits[day % len(splits)]
                muscles = SPLIT_MUSCLES[split]
                day_exercises = []
                if split in ["legs", "lower body"]:
                    for leg_part in ["quads", "hamstrings", "glutes", "calves"]:
                        leg_exs = []
                        for eq in equipment:
                            leg_exs += EXERCISES["legs"].get(leg_part, {}).get(eq, [])
                        if leg_exs:
                            day_exercises.append(random.choice(leg_exs))
                else:
                    for muscle in muscles:
                        day_exercises.extend(get_exercises_for_muscle(muscle, equipment, min_per_muscle=2))
                # Remove duplicates by exercise name
                seen = set()
                unique_exercises = []
                for ex in day_exercises:
                    if ex['name'] not in seen:
                        unique_exercises.append(ex)
                        seen.add(ex['name'])
                workout_plan.append({
                    "day": day + 1,
                    "split": split.title(),
                    "exercises": unique_exercises[:min_exercises_per_day],
                    "rest_between_exercises_seconds": 90
                })
    elif goal == "Increase Endurance & Athleticism":
        plyo_days = 0
        run_days = 0
        active_recovery_days = 0
        if days_per_week == 1:
            plyo_days = 1
            run_days = 1
        elif days_per_week == 2:
            plyo_days = 1
            run_days = 1
        elif days_per_week == 3:
            plyo_days = 2
            run_days = 1
        elif days_per_week == 4:
            plyo_days = 2
            run_days = 2
        elif days_per_week == 5:
            plyo_days = 3
            run_days = 2
        elif days_per_week == 6:
            plyo_days = 3
            run_days = 3
        elif days_per_week == 7:
            plyo_days = 3
            run_days = 3
            active_recovery_days = 1
        # For 1 day, combine plyo and run in one session
        if days_per_week == 1:
            plyo_exs = []
            for eq in equipment:
                plyo_exs += [ex for ex in CARDIO_PLYO_EXERCISES.get(eq, []) if 'run' not in ex['name'].lower()]
            if not plyo_exs:
                plyo_exs = [ex for ex in CARDIO_PLYO_EXERCISES["None"] if 'run' not in ex['name'].lower()]
            plyo_sample = random.sample(plyo_exs, k=min(4, len(plyo_exs)))
            for ex in plyo_sample:
                ex = ex.copy()
                ex['sets'] = 3
            running_workout = random.choice(RUNNING_WORKOUTS)
            run_ex = running_workout.copy()
            workout_plan.append({
                "day": 1,
                "split": "Plyometrics + Running Workout",
                "exercises": plyo_sample + [run_ex],
                "rest_between_exercises_seconds": 45
            })
        else:
            # Alternate plyo and run days as much as possible
            day_types = []
            n = plyo_days + run_days + active_recovery_days
            plyo_count = plyo_days
            run_count = run_days
            # For 7-day plan, insert active recovery on day 5
            if active_recovery_days:
                for i in range(n):
                    if i == 4:
                        day_types.append("active_recovery")
                    else:
                        # Alternate plyo and run, start with plyo
                        if plyo_count > 0 and (i % 2 == 0 or run_count == 0):
                            day_types.append("plyo")
                            plyo_count -= 1
                        elif run_count > 0:
                            day_types.append("run")
                            run_count -= 1
            else:
                for i in range(n):
                    # Alternate plyo and run, start with plyo
                    if plyo_count > 0 and (i % 2 == 0 or run_count == 0):
                        day_types.append("plyo")
                        plyo_count -= 1
                    elif run_count > 0:
                        day_types.append("run")
                        run_count -= 1
            for i, day_type in enumerate(day_types):
                if day_type == "plyo":
                    plyo_exs = []
                    for eq in equipment:
                        plyo_exs += [ex for ex in CARDIO_PLYO_EXERCISES.get(eq, []) if 'run' not in ex['name'].lower()]
                    if not plyo_exs:
                        plyo_exs = [ex for ex in CARDIO_PLYO_EXERCISES["None"] if 'run' not in ex['name'].lower()]
                    plyo_sample = random.sample(plyo_exs, k=min(4, len(plyo_exs)))
                    for ex in plyo_sample:
                        ex['sets'] = 3
                    workout_plan.append({
                        "day": len(workout_plan) + 1,
                        "split": "Plyometric Conditioning",
                        "exercises": plyo_sample,
                        "rest_between_exercises_seconds": 45
                    })
                elif day_type == "run":
                    running_workout = random.choice(RUNNING_WORKOUTS)
                    run_ex = running_workout.copy()
                    rest_between = run_ex.get("rest_seconds", 0) if run_ex.get("sets", 1) > 1 else None
                    workout_plan.append({
                        "day": len(workout_plan) + 1,
                        "split": "Running Workout",
                        "exercises": [run_ex],
                        **({"rest_between_exercises_seconds": rest_between} if rest_between else {})
                    })
                elif day_type == "active_recovery":
                    recovery_sample = random.sample(ACTIVE_RECOVERY, k=min(3, len(ACTIVE_RECOVERY)))
                    exercises = [
                        {"name": ex, "time_seconds": 60, "rest_seconds": 15, "description": ex}
                        for ex in recovery_sample
                    ]
                    workout_plan.append({
                        "day": len(workout_plan) + 1,
                        "split": "Active Recovery",
                        "exercises": exercises,
                        "rest_between_exercises_seconds": 30
                    })
        return workout_plan
    elif goal == "Lose Weight":
        # For 7 days: 3 running, 3 fat-burning, 1 active recovery (always on day 7)
        if days_per_week == 7:
            num_run = 3
            num_fat = 3
            num_recovery = 1
            day_types = []
            run_count = num_run
            fat_count = num_fat
            for i in range(7):
                if i == 6:
                    day_types.append("active_recovery")
                elif (i % 2 == 0 and run_count > 0) or fat_count == 0:
                    day_types.append("run")
                    run_count -= 1
                else:
                    day_types.append("fat")
                    fat_count -= 1
        else:
            # Determine number of running and fat-burning days
            num_run = days_per_week // 2 + (days_per_week % 2)
            num_fat = days_per_week // 2
            day_types = []
            run_count = num_run
            fat_count = num_fat
            for i in range(days_per_week):
                if (i % 2 == 0 and run_count > 0) or fat_count == 0:
                    day_types.append("run")
                    run_count -= 1
                else:
                    day_types.append("fat")
                    fat_count -= 1
        for i, day_type in enumerate(day_types):
            if day_type == "run":
                running_workout = random.choice(RUNNING_WORKOUTS)
                run_ex = running_workout.copy()
                rest_between = run_ex.get("rest_seconds", 0) if run_ex.get("sets", 1) > 1 else None
                workout_plan.append({
                    "day": len(workout_plan) + 1,
                    "split": "Running Workout",
                    "exercises": [run_ex],
                    **({"rest_between_exercises_seconds": rest_between} if rest_between else {})
                })
            elif day_type == "fat":
                fat_exs = []
                # Use best equipment available
                eq_priority = ["Full Gym", "Kettlebells", "Dumbbells", "None"]
                eq_used = None
                for eq in eq_priority:
                    if eq in equipment and FAT_BURNING_EXERCISES.get(eq):
                        eq_used = eq
                        break
                if not eq_used:
                    eq_used = "None"
                fat_exs = random.sample(FAT_BURNING_EXERCISES[eq_used], k=min(5, len(FAT_BURNING_EXERCISES[eq_used])))
                for ex in fat_exs:
                    ex['sets'] = 3
                workout_plan.append({
                    "day": len(workout_plan) + 1,
                    "split": "Fat-Burning HIIT",
                    "exercises": fat_exs,
                    "rest_between_exercises_seconds": 45
                })
            elif day_type == "active_recovery":
                recovery_sample = random.sample(ACTIVE_RECOVERY, k=min(3, len(ACTIVE_RECOVERY)))
                exercises = [
                    {"name": ex, "time_seconds": 60, "rest_seconds": 15, "description": ex}
                    for ex in recovery_sample
                ]
                workout_plan.append({
                    "day": len(workout_plan) + 1,
                    "split": "Active Recovery",
                    "exercises": exercises,
                    "rest_between_exercises_seconds": 30
                })
        return workout_plan

def add_descriptions_to_exercises():
    # Add description to EXERCISES
    for muscle in EXERCISES.values():
        for subgroup in muscle.values():
            for eq_list in subgroup.values():
                for ex in eq_list:
                    if 'description' not in ex:
                        ex['description'] = ex['name']
    # Add description to CARDIO_PLYO_EXERCISES
    for eq_list in CARDIO_PLYO_EXERCISES.values():
        for ex in eq_list:
            if 'description' not in ex:
                ex['description'] = ex['name']
add_descriptions_to_exercises()

def get_equipment_options():
    return EQUIPMENT_OPTIONS

def get_goal_options():
    return GOAL_OPTIONS

# Main function for HTML GUI integration
# Accepts: days_per_week (int), equipment (list of str), goal (str)
# Returns: workout plan (list of dicts)
def get_workout_plan(days_per_week, equipment, goal):
    return generate_workout(days_per_week, equipment, goal)