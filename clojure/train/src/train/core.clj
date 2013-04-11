(ns train.core)

(def sample-seat {:carriage "A", :number 3})
(def sample-reservation-request {:train-id "City of New Orleans"
                                 :seat-count 1})
(def sample-reservation-showing-only-required-fields {:train-id "City of New Orleans"
                                                      :seats [sample-seat]
                                                      :booking-reference "387829"})

(def sample-reservation (assoc sample-reservation-request
                               :seats [sample-seat]
                               :booking-reference "387829"))


 
