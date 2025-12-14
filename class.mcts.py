class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state  # هنا مخزن حالة اللعبة (اللوحة، مكان اللاعب A، مكان اللاعب B، والدور الحالي)
        self.parent = parent  # ده النود الأب اللي جابنا لحد هنا
        self.move = move  # الحركة اللي اتعملت عشان نوصل للحالة دي
        self.children = []  # لستة فاضية هنحط فيها النودز اللي هتتوسع من هنا
        self.visits = 0  # عدد المرات اللي اتزور فيها النود ده
        self.wins = 0  # عدد المكاسب اللي اتحققت من النود ده لصالح اللاعب اللي عمل الحركة

    def is_fully_expanded(self):
        board, posA, posB, turn = self.state  # بفك الحالة عشان أتعامل معاها
        current_pos = posA if turn == "A" else posB  # بشوف مين دوره دلوقتي وأجيب مكانه
        other_pos = posB if turn == "A" else posA  # وبجيب مكان الخصم
        moves = get_moves(current_pos, board, other_pos)  # بجيب كل الحركات اللي ممكن تتعمل من المكان الحالي
        return len(self.children) == len(moves)  # لو عدد ال (children) بيساوي عدد الحركات يبقى خلاص اتوسع كله

    def best_child(self, c=1.4):
        choices_weights = [
            (child.wins / child.visits) + c * math.sqrt((2 * math.log(self.visits) / child.visits))
            # هنا بحسب قيمة UCT لكل child: نسبة المكسب + عامل الاستكشاف
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]  
        # باختار الchild اللي عنده أعلى قيمة UCT
    def expand(self):
        board, posA, posB, turn = self.state  # بفك الحالة الحالية
        current_pos = posA if turn == "A" else posB  # مكان اللاعب اللي دوره
        other_pos = posB if turn == "A" else posA  # مكان الخصم
        moves = get_moves(current_pos, board, other_pos)  # الحركات المتاحة

        # بدور على الحركات اللي لسه ما توسعتش
        expanded_moves = [child.move for child in self.children]  # بجمع الحركات اللي اتعملت قبل كده
        for move in moves:  # بلف على كل حركة ممكنة
            if move not in expanded_moves:  # لو الحركة دي لسه ما اتعملتش
                new_board = [row[:] for row in board]  # بعمل نسخة جديدة من البورد (عشان ما أعدلش في الأصلية)
                new_board[current_pos[0]][current_pos[1]] = BLOCK  # المكان اللي كنت فيه بيتقفل (block)
                new_posA = move if turn == "A" else posA  # لو اللاعب A هو اللي لعب، مكانه يتغير
                new_posB = move if turn == "B" else posB  # لو اللاعب B هو اللي لعب، مكانه يتغير
                new_turn = "B" if turn == "A" else "A"  # الدور يتبدل للخصم
                new_state = (new_board, new_posA, new_posB, new_turn)  # الحالة الجديدة بعد الحركة
                child = MCTSNode(new_state, parent=self, move=move)  # بعمل نود جديد للحالة دي
                self.children.append(child)  # أضيفه كchild للنود الحالي
                return child  # أرجع الchild الجديد اللي اتعمل
        return None  # لو مفيش حركات جديدة يبقى مفيش توسع

