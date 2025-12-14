def create_board():
    # الدالة دي بتنشئ لوحة جديدة للعبة
    # كل خانة في اللوحة هتكون فاضية في البداية (EMPTY)
    # وبتكون اللوحة مربعة بحجم SIZE × SIZE

    board = [
        [EMPTY for _ in range(SIZE)]  # لكل عمود في الصف، حط EMPTY
        for _ in range(SIZE)          # كرر ده لكل صف في اللوحة
    ]
    # النتيجة: مصفوفة ثنائية الأبعاد (2D list) بحجم SIZE × SIZE،
    # وكل خانة فيها EMPTY

    return board  # ارجع اللوحة الجديدة