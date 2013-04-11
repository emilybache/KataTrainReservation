(ns train.core
  (:require [clojure.set :as set]))

(declare train-reserved-seats)


(defn train-configuration [id]
  )



(defn train-state [id]
  )

(defn train-available-seats [id]
  (set/difference (train-configuration id) (train-reserved-seats id)))

(defn reserve-train-seats [train request-count]
  (take request-count train))

(defn make-reservation [reservation-request]
  (assoc reservation-request
         :seats (reserve-train-seats (train-available-seats (:train-id reservation-request))
                                     (:seat-count reservation-request))))

