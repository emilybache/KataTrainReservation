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
  (prerequisite (take-seats 1 [..1.. ..2..]) => [..2..])
  (let [result (make-reservation {:train-id ..id.. :seat-count 1}
                                 {..id.. [..1.. ..2..]})]
    (:fleet-snapshot result) => {..id.. [..1..]}
    (:reservation result) => (contains {:train-id ..id.., :seats [..2..]})))
