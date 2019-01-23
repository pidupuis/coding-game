(ns Player
  (:gen-class))

(defn -main [& args]
  (while true
    (let [mountains (repeatedly 8 read)]
        (println 
            (.indexOf mountains (apply max mountains))))))
