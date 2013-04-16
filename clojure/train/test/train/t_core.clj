(ns train.t-core
  (:use midje.sweet)
  (:use train.core)
  (:require [clojure.set :as set]))

(def sample-seat {:coach "A", :seat-number 3})
(def sample-reservation-request {:train-id "local_1000"
                                 :seat-count 1})
(def sample-reservation-showing-only-required-fields {:train-id "local_1000"
                                                      :seats [sample-seat]
                                                      :booking-reference "387829"})

(def sample-reservation (assoc sample-reservation-request
                               :seats [sample-seat]
                               :booking-reference "387829"))


(fact "you can reserve seats"
  "TODO: Write code here")
