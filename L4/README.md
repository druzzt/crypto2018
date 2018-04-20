(Algorithmic/security track) Implement Merkle-Puzzle cryptosystem http://www.merkle.com/1974/PuzzlesAsPublished.pdf (read the story behind: http:// www.merkle.com/1974/). Run your system for N = 2n, where n = 24,32,40 and compute and/or estimate space and time requirements. You need to prepare a presentation of the system with n = 24 (at least).



----------------------
[Tutorial](https://medium.com/100-days-of-algorithms/day-75-merkles-puzzles-d9f0e8f9c9d0)
[Explanation](http://blog.press.princeton.edu/2017/01/09/cipher-challenge-1-from-joshua-holden-merkles-puzzles/)
----------------------
The Method
The method used is based on a single concept: that ofa "puzzle." We defme a puzzle as a cryptogram which is meant to be broken. To solve the puzzle, we must cryptanalyze the cryptogram. Having done this, we learn the information that was "enpuzzled," the plaintext of the cryptogram. Just as we can encrypt plaintext to produce a cryptogram, so we can enpuzzle information to produce a puzzle. A puzzle, though, is meant to be solved, while ideally, a cryptogram cannot be cryptana- lyzed. To solve a puzzle, all one need do is put in the required amount of effort.
To sharpen our defmition, we will consider the fol- lowing method of creating puzzles. First, select a strong encryption function. We are not interested in the details of how this encryption function works: our only interest is that it does work. The reader can select any encryption function that he feels is particularly strong and effective. A concrete example might be the Lucifer encryption function [2], which is currently felt to be quite strong.
After selecting an encryption function, we create our puzzle by encrypting some piece ofinformation with that function. Of course, if our encryption function is really good, our puzzle is unsolvable, which is not what we want. To avoid this problem, we artificially restrict the size of the key space used with the encryption function. If the key is normally 128 bits, we might use only 30 bits. While searching through 21128 possible keys seems completely infeasible, searching through 2130 is tedious,
but quite possible. We can control the difficulty of solving a puzzle, simply by changing the restriction on the size ofthe key space used. To make the puzzle harder to solve, we might select a 40 bit key, while to make it easier, we might select a 20 bit key.
The puzzles we create by this method are precisely as difficult to break as we desire. We rely on the strength of the underlying encryption function to insure that our puzzle can only be solved by exhaustive search through
296
the key space, and we adjust the size ofthe key space to control the difficulty of solving the puzzle.
There is still one more point that must be brought out. In cryptanalyzing an encrypted message, the crypt- analyst relies on the redundancy in the message. I f the information we enpuzzle is random, there will be no redundancy, and thus no way of solving the puzzle. We must deliberately introduce redundancy into our puzzle, so that it can be solved. This can be done easily enough by encrypting, along with the information, a constant that is known to X, Y, and Z. When we try to decrypt the puzzle with a particular key, then the recovery ofthis constant part can be taken as evidence that we have selected the right key, and thus have solved the puzzle. Contrariwise, the absence of the constant part in the decrypted puzzle indicates that we have used the wrong key, and should try again.
With the concept of "puzzle" in hand, we can pro- ceed. We let X and Y agree upon the value of N which they wish to use. X then generates N puzzles, and trans- mits these N puzzles to Y over the key channel. X chooses the size of the key space so that each puzzle requires O(N) efforts to break. (That is, X selects a key space of size C*N, for a constant, C.) Each puzzle contains, within itself, two pieces ofinformation. Neither piece of information is readily available to anyone ex- amining the puzzle. By devoting O(N) effort to solving the puzzle, it is possible to determine both these pieces of information. One piece of information is a puzzle 10, which uniquely identifies each of the N puzzles. The IO's were assigned by X at random. The other piece of information in the puzzle is a puzzle key, i.e, one of the possible keys to be used in subsequent encrypted com- munications. To distinguish the puzzle keys, one for each puzzle, from the keys randomly selected from the re- stricted key space to create the puzzles, we will call the former "puzzle keys," and the latter, "random keys." Thus, N puzzle keys are enpuzzled, and in the process of enpuzzling each puzzle key, a random key is used. (The puzzle key is also selected by X at random.)
When Y is presented with this menu of N puzzles, he selects a puzzle at random, and then spends the amount of effort required to solve the puzzle. Y then transmits the 10 back to X over the key channel, and uses the puzzle key found in the puzzle as the key for further encrypted communications over the normal channel.
At this point, we summarize who knows what. X, Y, and Z all know the N puzzles. They also know the 10, because Y transmitted the 10 over the key channel. Y knows the corresponding puzzle key, because Y solved the correct puzzle. X knows the corresponding puzzle key, because X knows which puzzle key is associated with the 10 that Y sent. Z knows only the 10, but does not know the puzzle key. Z cannot know which puzzle contains the puzzle key that Y selected, and which X and Y are using, even though he knows the 10. To determine which puzzle is the correct one, he must break puzzles at random until he encounters the correct one.

 If Z desires to determine the key which X and Y are using, then, on an average, Z will have to solve H) N puzzles before reaching the puzzle that Y solved. Each puzzle has been constructed so that it requires O(N) effort to break, so Z must spend, on an average, O(Nj2) effort to determine the key. Y, on the other hand, need only spend O(N) effort to break the one puzzle he selected, while X need only spend O(N) effort to man- ufacture the N puzzles. Thus, both X and Y will only put in O(N) effort.
Having given an outline of the method, we shall now tum to a detailed look at its implementation. Before proceeding, a few points of notation must be cleared up. F will be used to designate an encryption function. Note that F can be any encryption function the reader feels is particularly powerful and effective. F will accept an arbitrary number ofarguments. The fust argument is the key, and remaining arguments are the message to be encrypted. All of the data objects will be bit strings of arbitrary length. We imagine that the bit strings that make up the message are first concatenated into one long bit string, which is then encrypted using F. To illustrate, we might have the following call on F:
F(IOOIOIOIIO,OIIIIOIOOOOI, 01000000101101011,(010111)
The fust bit string is to be used as the key, and the remaining three bit strings form the message.
We shall also use the function, RAND. RAND(P) gen- erates a random number between I and P, inclusive. Note that the normal random number generator on a computer is not suited for this. We require either truly random numbers, or pseudorandom numbers generated by a very powerful pseudorandom number generator. Of course, such a pseudorandom number generator will have to be initialized with a truly random seed.
When we have finished making the puzzle, we will transmit it using the function, TRANSMIT( ARG).

To summarize:
N Total number of puzzles.
C Arbitrary constant. The random key is selected
from a key space ofsize.C*N.
F A strong encryption function. Its inverse is
called "FINVBRSB"
In the algorithm presented, we generate neither the ID's
nor the puzzle keys at random. The ID's are generated by encrypting the numbers I through N. With a good encryption function, this can be viewed as a method of generating pseudorandom numbers. The puzzle keys are generated by encrypting the ID's. Again, this can be viewed as a good pseudorandom number generator. It has the additional property that the puzzle key can be quickly and easily generated from the ID. Two auxiliary keys, K I and K2, are used in these two encryption proc- esses, and provide the truly random "seed" for these somewhat unorthodox pseudorandom number genera- tors.
Using these conventions, we can write the algorithm for X, who is generating the puzzles, in the following fashion:
```
var ID. KEY. CONSTANT. RANDOMKEY, PUZZLE. K I. K2:bit string;
begin
K I:=RAND(LARGE); K2:=RAND( LARGE); CONSTANT:=RAND( LARGE); TRANSMIT( CONSTANT);
for 1:=1 to N do begin
ID:=F(Kl,I);
KEY:=F( K2,ID);
RANDOMKEY:<=&RAND( C*N);
PUZZLE:=F( RANDOMKEY. lD. KEY. CONSTANT);
TRANSMIT( PUZZLE);
end; end;
```
We can now write Y's code. We will need a new primitive for Y: RECEIVE(ARG) is a procedure which returns the value of the next puzzle in ARG. We also need to clarify some notation. I f we encrypt some argu- ments with F, we wish to be able to decrypt those arguments. If we say:
```
CIPHERT.EXT:=F( SOMBKBY.A,B,C);
we want to be able to invert this by saying:
A,B,C:=FINVBRSE( SOMBKEY,CIPHBRTEXT);
```
The meaning of this should be obvious, in spite of the fact that we have three variables, A, B, and C on the left hand side of the assignment statement. With these ad- ditional conventions, the code for Y would then appear as follows:
```
var ID, KEY, CONSTANT, SELECTEDPUZZLEID, THEPUZZLE, CURRENTPUZZLE,
TEMPCONSTANT:bil string;
begin
SELECTEDPUZZLEID:=RAND( N); RECEIVE( CONST ANT);
for I := 1 to N do
begin
RECEIVE( CUItRENTPUZZU);
if I=SELECTEDPUZZLEID thea THE PUZZLE:= CURRENTPUZZLE;
end;
comment follows;
The computation to fmd the randomkey used by A
for 1:= 1 to c*Ndo begin
ID.KEY.TEMPCONSTANT:=FINVERSE • (I.THEPUZZLE);
if TEMpcONSTANT=CONSTANT then goto DONE;
end;
print("should not reach this point."); panic;
DONE: TRANSMIT(ID); end;
```

At the very end, X must receive the ID that Y transmitted, and deduce the key. The last actions that X must perform are as follows:
```
begin
RECE'VE( 10):
KEV:=P( K2,1D);
comment KEY now has the same value in both X and Y. All they
have to do is use KEY as the key with which to encrypt further
transmissions. end:
```
The only information available to Z is the code executed by X and Y, and the values actually transmitted over the key channel. Thus, Z is in possession of N, the CONSTANT, the ID that Y transmitted to X, and also the puzzles that X transmitted to Y. All other variables are known either exclusively by X, or exclusively by Y.
In summary: the method allows the use of channels satisfying assumption I, and not satisfying assumption 2, for the transmission of key information. We need only guarantee that messages are unmodified, and we no longer require that they be unread. If the two commu- nicants, X and Y, put in O(N) effort, then the third person, Z, must put in O(Nf2) effort to determine the key. We now tum to the consideration of various impli- cations of this work.





------------------------
# N=18:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b'nR9=\xfe\\y=\x1c\xcc\xc27\xe1\x8cG\xcd'
index: 123452
steps executed: 29634
Alice has secret
key: b'nR9=\xfe\\y=\x1c\xcc\xc27\xe1\x8cG\xcd'
adversary failed to find secret
searched puzzles: 93 steps executed: 2966233

real	0m32.864s
user	0m31.642s
sys	0m0.899s
```
# N=19:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b" \xab\x17h\x18p\xb9}5\xd3'\xc1\x8a\xe2\xfa\x06"
index: 460287
steps executed: 30347
Alice has secret
key: b" \xab\x17h\x18p\xb9}5\xd3'\xc1\x8a\xe2\xfa\x06"
adversary failed to find secret
searched puzzles: 91 steps executed: 3043805

real	0m37.075s
user	0m35.477s
sys	0m1.481s
```
# N=20:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b'H/\xacN\x91\x97F9\xceZ\xb3\xed\x8c\xf7\xe3-'
index: 991277
steps executed: 18754
Alice has secret
key: b'H/\xacN\x91\x97F9\xceZ\xb3\xed\x8c\xf7\xe3-'
adversary failed to find secret
searched puzzles: 58 steps executed: 1882092

real	0m35.331s
user	0m32.254s
sys	0m2.873s
```
# N=21:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b"\x95L\x86\xf4\xca\x97'%O\xd4+Is\xd5\xfeo"
index: 892925
steps executed: 9267
Alice has secret
key: b"\x95L\x86\xf4\xca\x97'%O\xd4+Is\xd5\xfeo"
adversary failed to find secret
searched puzzles: 27 steps executed: 940036

real	0m44.631s
user	0m38.576s
sys	0m5.746s
```
# N=22:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b'>.\xc0\xd0\xcb\xa1\x13\x10\xe4\x9eI\x18o\x1ar\xc3'
index: 1115269
steps executed: 12519
Alice has secret
key: b'>.\xc0\xd0\xcb\xa1\x13\x10\xe4\x9eI\x18o\x1ar\xc3'
adversary failed to find secret
searched puzzles: 39 steps executed: 1272620

real	1m22.993s
user	1m11.359s
sys	0m11.206s
```
# N=23:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b'\x8a_(\x83^9\xaa?\x98\x01f\x01f\xe6\x89\x1e'
index: 7546860
steps executed: 9451
Alice has secret
key: b'\x8a_(\x83^9\xaa?\x98\x01f\x01f\xe6\x89\x1e'
adversary failed to find secret
searched puzzles: 30 steps executed: 956101

real	2m32.625s
user	2m9.353s
sys	0m22.529s
```
# N=24:
```
Arq:L4 me$ time python3 merklePuzzle.py 
Bob has secret and publishes index
key: b'`\x9f\x13\xe5\xfe\xcd\x13\x02xB\xdb\xd1t\xdaK"'
index: 13200823
steps executed: 56835
Alice has secret
key: b'`\x9f\x13\xe5\xfe\xcd\x13\x02xB\xdb\xd1t\xdaK"'
adversary failed to find secret
searched puzzles: 169 steps executed: 5686280

real	5m44.152s
user	4m56.175s
sys	0m45.584s
```