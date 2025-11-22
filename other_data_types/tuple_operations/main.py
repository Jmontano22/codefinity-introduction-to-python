# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")
#coverting shelf1 to tuple
# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
shelf1_update.tuple(shelf1)

shelf1_concat = shelf1_update + shelf1

shelf1_concat.count("celery")

shelf1_concat.index("f")