(ns train.t-core
  (:use midje.sweet)
  (:use train.core)
  (:require [clojure.set :as set]))

(def sample-seat {:carriage "A", :number 3})
(def sample-reservation-request {:train-id "City of New Orleans"
                                 :seat-count 1})
(def sample-reservation-showing-only-required-fields {:train-id "City of New Orleans"
                                                      :seats [sample-seat]
                                                      :booking-reference "387829"})

(def sample-reservation (assoc sample-reservation-request
                               :seats [sample-seat]
                               :booking-reference "387829"))


 
(fact "you can reserve a single seat"
  (make-reservation {:train-id ..id.., :seat-count 1}) => (contains {:seats [..chosen-seat..]
                                                                     :train-id ..id..})
  (provided
    (train-available-seats ..id..) => ..available-seats..
    (reserve-train-seats ..available-seats.. 1) => [..chosen-seat..]))
  
(fact "you can reserve N train seats"
  (let [available-seats #{..1.. ..2.. ..3..}
        reserved-seats (reserve-train-seats available-seats 2)]
    (count (set/difference available-seats reserved-seats)) => 1))

(fact "you can construct available seats from two services"
  (train-available-seats ..id..) => #{..1.. ..3..}
  (provided
    (train-configuration ..id..) => #{..1.. ..2.. ..3..}
    (train-reserved-seats ..id..) => #{..2..}))
    
