# simple-matching-engine-python

#### SUB juhb B foo 10 450
#### SUB bpjl B foo 7 500
#### SUB lpqn B foo 10 1000
#### SUB jyfu S foo 10 1200
#### SUB zqcu S foo 15 400
#### CXL zqcu
#### END
<br>

### after order lpqn, the OB is 
### B: ['450@10#juhb', '1000@l0#pqn', '500@7#bpjl']
### S: []
### after order jyfu. the OB is 
### B: ['250@l0#pqn', '500@7#bpjl']
### S: []
<br>

## Result of my code:
```
SUB juhb B foo 10 450
B: ['450@10#juhb']
S: []
SUB bpjl B foo 7 500
B: ['450@10#juhb', '500@7#bpjl']
S: []
SUB lpqn B foo 10 1000
B: ['450@10#juhb', '1000@10#lpqn', '500@7#bpjl']
S: []
SUB jyfu S foo 10 1200
B: ['250@10#lpqn', '500@7#bpjl']
S: []
SUB zqcu S foo 15 400
B: ['250@10#lpqn', '500@7#bpjl']
S: ['400@15#zqcu']
CXL zqcu
B: ['250@10#lpqn', '500@7#bpjl']
S: []
END
```
