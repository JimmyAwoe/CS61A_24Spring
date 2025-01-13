(define (ascending? s) 
    (if (or (null? s) (null? (cdr s))) 
        #t
        (if (>= (car (cdr s)) (car s))
            (ascending? (cdr s))
            #f)))

(define (my-filter pred s) 
    (if (null? s)
        nil
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s)))
        ))

(my-filter even? (list 1 2 3 4 5))

(define (interleave lst1 lst2)
    (define (insert_1 lst1 lst2)
        (if (null? lst1) lst2 (cons (car lst1) (insert_2 (cdr lst1) lst2))))
    (define (insert_2 lst1 lst2)
        (if (null? lst2) lst1 (cons (car lst2) (insert_1 lst1 (cdr lst2)))))
    (insert_1 lst1 lst2))    


(define (no-repeats s)
  (if (null? s) s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))))
