(ns train.core
  (:use [midje.sweet :only [unfinished]])
  (:require [clojure.set :as set]))

(unfinished take-seats)




(defn make-reservation [request fleet-snapshot]
  (let [seats-found (take-seats (:seat-count request)
                                (get fleet-snapshot (:train-id request)))]
    {:fleet-snapshot ["fred"]
     :reservation (assoc request :seats seats-found)}))
 
