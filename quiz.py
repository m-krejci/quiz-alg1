import hashlib
import re
import io


class Challenges:
    # Returns the maximum value from the input array
    def mad_max(self, a: list[int]) -> int:
        maxed = a[0]
        for i in range(len(a)):
            if a[i] > maxed:
                maxed = a[i]
        return maxed

    # Returns the sum of all numbers in the input array
    def sumo(self, a: list[int]) -> int:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        return sum

    # Reads all lines from the input (manual). Each line contains numbers 
    # separated by spaces. Each number that is at most as large as 
    # the threshold value (max_threshold) is written to a separate line in the 
    # output.
    def rtfm(self, manual: io.StringIO, output: io.StringIO, max_threshold: int) -> None:
        # TODO: Implement the solution
        for line in manual:
            nums = line.split()

            for num in nums:
                if int(num) <= max_threshold:
                    output.write(f"{num}\n")

    # Tests if the non-negative integer represented as a string is divisible by three.
    # The number is given as a string of digits (0-9) and may contain leading zeros.
    def div_three(self, s: str) -> bool:
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])
        if sum % 3 == 0:
            return True
        return False
    

    def remove_duplicates(self, a: list[int]) -> list[int]:
        my_set = set()
        ret_list = []
        for i in range(len(a)):
            if a[i] not in my_set:
                my_set.add(a[i])
                ret_list.append(a[i])
        return ret_list

    # Returns the fifth largest element in the array (after removing duplicates).
    # If there are fewer than five distinct elements, returns the smallest element.
    def high_five(self, a: list[int]) -> int:
        # TODO: Implement the solution
        new_list = self.remove_duplicates(a)
        if len(new_list) < 5:
            smallest = new_list[0]
            for i in range(len(new_list)):
                if smallest > new_list[i]:
                    smallest = new_list[i]
            return smallest
        else:
            new_list.sort()
            return new_list[len(new_list)-5]

    # Returns the count of occurrences of the most frequent element in the array.
    # The numbers in the array are relatively small non-negative integers.
    def duplo(self, a: list[int]) -> int: 
        # TODO: Implement the solution
        elem = {}
        for num in a:
            if num in elem:
                elem[num] += 1
            else:
                elem[num] = 1
        max = 0
        for key in elem:
            if elem[key] > max:
                max = elem[key]
        return max


# Returns true if the sum of the elements below the main diagonal of the matrix
# is greater than the sum of the elements above the main diagonal. The matrix is
# square and given by rows, so m[i] gives the ith row of the matrix.
    def matrix(self, m: list[list[int]]) -> bool:
        above = list()
        under = list()
        for i in range(len(m)):
            for j in range(len(m)):
                if i == j:
                    continue
                if i < j:
                    above.append(m[i][j])
                if i > j:
                    under.append(m[i][j])
        under_sum = self.sumo(under)
        above_sum = self.sumo(above)
        return under_sum > above_sum
    
    # Returns the number of lonely knights on a square chessboard. 
    # A knight is lonely if no square within a knight's move is occupied by another knight.
    def lonely_knights(self, m: list[list[int]]) -> int:
        # TODO: Implement the solution
        lonely = 0
        occ = 0
        row_len = len(m[lonely])
        col_len = len(m)
        for row in range(row_len):
            for col in range(col_len):
                if m[row][col] == 0:
                    continue
                else:
                    lonely += 1
                    # 1
                    if (row-2 >= 0 and row-2 <= row_len-1) and (col-1 >= 0 and col-1 <= col_len-1):
                        if m[row-2][col-1] == 1:
                            occ += 1
                            continue
                    # 2
                    if (row-2 >= 0 and row-2 <= row_len-1) and (col+1 >= 0 and col+1 <= col_len-1):
                        if m[row-2][col+1] == 1:
                            occ += 1
                            continue
                    # 3
                    if (row-1 >= 0 and row-1 <= row_len-1) and (col-2 >= 0 and col-2 <= col_len-1):
                        if m[row-1][col-2] == 1:
                            occ += 1
                            continue
                    # 4
                    if (row-1 >= 0 and row-1 <= row_len-1) and (col+2 >= 0 and col+2 <= col_len-1):
                        if m[row-1][col+2] == 1:
                            occ += 1
                            continue
                    # 5
                    if (row+1 >= 0 and row+1 <= row_len-1) and (col-2 >= 0 and col-2 <= col_len-1):
                        if m[row+1][col-2] == 1:
                            occ += 1
                            continue
                    # 6
                    if (row+1 >= 0 and row+1 <= row_len-1) and (col+2 >= 0 and col+2 <= col_len-1):
                        if m[row+1][col+2] == 1:
                            occ += 1
                            continue
                    # 7
                    if (row+2 >= 0 and row+2 <= row_len-1) and (col-1 >= 0 and col-1 <= col_len-1):
                        if m[row+2][col-1] == 1:
                            occ += 1
                            continue
                    # 8
                    if (row+2 >= 0 and row+2 <= row_len-1) and (col+1 >= 0 and col+1 <= col_len-1):
                        if m[row+2][col+1] == 1:
                            occ += 1
                            continue
        return lonely-occ



###############################################################################
## Self-evaluation code (ignore this part)                                   ##
###############################################################################
class Quiz(Challenges):
    
    def _MadMax(self, a):
        return self.mad_max(a)

    def _Sumo(self, a):
        return self.sumo(a)

    def _DivThree(self, a):
        return self.div_three(self.ToString(a, ""))
    
    def _HighFive(self, a):
        return self.high_five(a)
    
    def _Duplo(self, a):
        return self.duplo(a)
    
    def _Matrix(self, a):
        return self.matrix(self.ToMatrix(a))
    
    def _LonelyKnights(self, a):
        return self.lonely_knights(self.ToMatrix(a))
    
    def _RTFM(self, a):
        w = io.StringIO()
        self.rtfm(self.CreateTextReader(self.ToMatrix(a)), w, 50)
        s = self.NormalizeNewline(w.getvalue())
        w.close()
        if s.endswith("\n"):
            s = s[:s.rfind("\n")]
        return s

    def testChallenges(self):
        self.rnd = RandomNumberGenerator()
        
        # Challenge names, functions, configurations, and cummulative proofs (MD5 hashes)
        # If you change anything, the proofs will no longer match and will have to be recomputed.
        names = ["MadMax", "Sumo", "RTFM", "DivThree", "HighFive", "Duplo", "Matrix", "LonelyKnights"]
        challenges = [self._MadMax, self._Sumo, self._RTFM, self._DivThree, self._HighFive, self._Duplo, self._Matrix, self._LonelyKnights]
        N = [
            [5, 7, 8 * 8, 20, 30, 10, 5 * 5, 8 * 8],
            [100, 700, 64 * 64, 200, 300, 1000, 64 * 64, 8 * 8],
            [300, 70000, 256 * 256, 20000, 3000, 10000, 256 * 256, 8 * 8]
        ]
        limits = [
            [1200, 17, 200, 10, 15000, 7, 700000, 2],
            [1000000, 17, 200, 10, 75000, 5, 2, 2],
            [2047, 1000, 200, 10, 15000, 15000, 1300, 2]
        ]
        proof = [
            "96cedf49031ccf65f92e7af58b5c74e4",  # MadMax
            "7df9b107c2835f82035bb7b09b16ed5e",  # Sumo
            "fc62b2d18469b31f8dfeec51ff16191d",  # RTFM
            "5dfd3f9e8e53e7dc166b6bd6dbba0453",  # DivThree
            "d23ad695ffbd5d6e7f9d9d14b1076450",  # HighFive
            "158634f351379d234fedcd0766417533",  # Duplo
            "c36dc181f24f7867f66ee93f5573d26c",  # Matrix
            "3b82a8b1767b9db8362d61815251c45d",  # LonelyKnights
        ]

        md5_hash = hashlib.md5()
        signature = "" # MD5 of the previous MD5 + the solution
        score = 0      # How many challenges were solved
        cipher = []    # Cummulates MD5 hashes of solutions
        
        # Try to solve all challenges. Compute signatures of answers
        failed = False
        for x in range(len(challenges)):
            signature = ""
            try:
                for i in range(3 * len(N)):
                    a = self.Rnd(N[i % len(N)][x], limits[i % len(N)][x])
                    result = str(challenges[x](a))
                    signature = self.GetMd5(md5_hash, signature + " " + result)
                    cipher.append(self.GetMd5(md5_hash, result))
            except Exception as ex:
                print("Exception:", ex)
            
            # Check the signature of solutions against the proof.
            passed = proof[x] == signature
            print(f"Challenge {names[x]}: {'Yeah!' if passed else 'Wrong answer'}")
            failed |= not passed
            score += 1 if passed else 0

        if failed:
            # Not passed => goodbye
            print("\"The way is shut. It was made by those who are Dead, and the Dead keep it, until the time comes. The way is shut.\" J.R.R. Tolkien, Return of the King")
        else:
            # Passed all the tests. Really? Then decode the final message.
            key = self.GetMd5(md5_hash, ''.join(cipher))
            proof = self.Decode("I@D8x2zGAcL:GuH(#.rJV9fJ7%GIqG?>&2B=&4n3An=??lH'dCgTN@sS3%BCh6Y>o8?Eg=&8>u@jWC]0,]Ap", key)
            print(f"PROOF: {proof}")
            
        print(f"SCORE: {score} / {len(challenges)}")

    def Rnd(self, n, limit):
        return self.rnd.rnd_array(n, limit)

    def ToString(self, a, sep):
        return sep.join(map(str, a))

    def ToMatrix(self, a):
        n = 1
        while (n + 1) * (n + 1) <= len(a):
            n += 1
        matrix = [[a[i * n + j] for j in range(n)] for i in range(n)]
        return matrix

    def CreateTextReader(self, matrix):
        sb = io.StringIO()
        for row in matrix:
            sb.write(' '.join(map(str, row)) + "\n")
        return io.StringIO(sb.getvalue())

    @staticmethod
    def GetMd5(md5_hash, input):
        return hashlib.md5(input.encode()).hexdigest()

    newline_regexp = re.compile(r"\r\n?|\n")

    @staticmethod
    def NormalizeNewline(str):
        return re.sub(Quiz.newline_regexp, "\n", str)

    @staticmethod
    def Decode(s, key):
        return ''.join(chr(32 + ((ord(c) - 32 + (127 - 32) - ord(key[i % len(key)])) % (127 - 32))) for i, c in enumerate(s))

# Random number generator - taken from OpenJDK
class RandomNumberGenerator:
    multiplier = 0x5DEECE66D
    addend = 0xB
    mask = (1 << 48) - 1

    def __init__(self, seed=0xDEADBEEF):
        # Initialize seed
        self.seed = (seed ^ self.multiplier) & self.mask

    def next(self, bits):
        # Random number generator logic taken from OpenJDK
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return int(self.seed >> (48 - bits))

    def rnd(self, bound):
        # Generate a random number with a bound
        r = self.next(31)
        m = bound - 1
        if (bound & m) == 0:  # Check if the bound is a power of 2
            r = int((bound * r) >> 31)
        else:
            while True:
                u = r
                r = u % bound
                if u - r + m >= 0:
                    break
                r = self.next(31)
        return r

    def rnd_array(self, n, limit):
        # Generate an array of random numbers
        a = []
        for _ in range(n):
            a.append(self.rnd(limit))
        return a

###############################################################################
## Runs the quiz                                                             ##
###############################################################################
if __name__ == "__main__":
    q = Quiz()
    q.testChallenges()
