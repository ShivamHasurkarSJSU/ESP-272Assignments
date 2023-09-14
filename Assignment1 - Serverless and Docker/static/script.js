document.addEventListener("DOMContentLoaded", function() {
    let board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ];
    let currentPlayer = 'X';
    let scores = { 'X': 0, 'O': 0 };
    let singlePlayer = false;
    let firstMove = true;

    document.getElementById('board').addEventListener('click', function(e) {
        if (e.target.classList.contains('cell')) {
            const row = Math.floor(e.target.dataset.index / 3);
            const col = e.target.dataset.index % 3;

            if (board[row][col] === '') {
                board[row][col] = currentPlayer;
                e.target.textContent = currentPlayer;

                if (checkWin(board, currentPlayer)) {
                    setTimeout(() => {
                        alert(`${currentPlayer} wins!`);
                        scores[currentPlayer]++;
                        updateScoreBoard();
                        resetBoard();
                    }, 100);
                    return;
                } else if (checkDraw(board)) {
                    setTimeout(() => {
                        alert('The game is a draw!');
                        resetBoard();
                    }, 100);
                    return;
                }

                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';

                if (singlePlayer && currentPlayer === 'O') {
                    if (firstMove) {
                        firstMove = false;
                        currentPlayer = 'X';
                        return;
                    }
                    bestMove();
                    if (checkWin(board, 'O')) {
                        setTimeout(() => {
                            alert('O wins!');
                            scores['O']++;
                            updateScoreBoard();
                            resetBoard();
                        }, 100);
                        return;
                    } else if (checkDraw(board)) {
                        setTimeout(() => {
                            alert('The game is a draw!');
                            resetBoard();
                        }, 100);
                        return;
                    }
                    currentPlayer = 'X';
                }
            }
        }
    });

    document.getElementById('singlePlayer').addEventListener('click', function() {
        singlePlayer = true;
        resetBoard();
    });

    document.getElementById('multiPlayer').addEventListener('click', function() {
        singlePlayer = false;
        resetBoard();
    });

    function updateScoreBoard() {
        document.getElementById('scoreBoard').textContent = `X: ${scores['X']} | O: ${scores['O']}`;
    }

    function resetBoard() {
        board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ];
        document.querySelectorAll('.cell').forEach(cell => cell.textContent = '');
    }

    function makeRandomMove() {
        let emptyCells = [];
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i][j] === '') {
                    emptyCells.push([i, j]);
                }
            }
        }

        if (emptyCells.length > 0) {
            const randomIndex = Math.floor(Math.random() * emptyCells.length);
            const [row, col] = emptyCells[randomIndex];
            board[row][col] = 'O';
            document.querySelector(`[data-index='${3 * row + col}']`).textContent = 'O';
        }
    }

    function checkWin(board, player) {
        for (let i = 0; i < 3; i++) {
            if (board[i][0] === player && board[i][1] === player && board[i][2] === player) {
                return true;
            }
            if (board[0][i] === player && board[1][i] === player && board[2][i] === player) {
                return true;
            }
        }
        if (board[0][0] === player && board[1][1] === player && board[2][2] === player) {
            return true;
        }
        if (board[0][2] === player && board[1][1] === player && board[2][0] === player) {
            return true;
        }
        return false;
    }

    function checkDraw(board) {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i][j] === '') {
                    return false;
                }
            }
        }
        return true;
    }

    function bestMove() {
        let maxEval = -Infinity;
        let move;
    
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i][j] === '') {
                    board[i][j] = 'O';
                    const eval = minimax(board, 0, false);
                    board[i][j] = '';
                    if (eval > maxEval) {
                        maxEval = eval;
                        move = { i, j };
                    }
                }
            }
        }
    
        board[move.i][move.j] = 'O';
        document.querySelector(`[data-index='${3 * move.i + move.j}']`).textContent = 'O';
    }    

    function minimax(board, depth, maximizing) {
        if (checkWin(board, 'O')) return 10 - depth;
        if (checkWin(board, 'X')) return depth - 10;
        if (checkDraw(board)) return 0;
    
        if (maximizing) {
            let maxEval = -Infinity;
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    if (board[i][j] === '') {
                        board[i][j] = 'O';
                        const eval = minimax(board, depth + 1, false);
                        board[i][j] = '';
                        maxEval = Math.max(eval, maxEval);
                    }
                }
            }
            return maxEval;
        } else {
            let minEval = Infinity;
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    if (board[i][j] === '') {
                        board[i][j] = 'X';
                        const eval = minimax(board, depth + 1, true);
                        board[i][j] = '';
                        minEval = Math.min(eval, minEval);
                    }
                }
            }
            return minEval;
        }
    }
    
});