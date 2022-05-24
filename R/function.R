cas_kable <- function(data, caption){
  tbl <- kable(data , caption = caption, align = 'c')
  return(tbl)
}

read_pickle <- function(filename){
  pd <- import("pandas")
  pickle_data <- pd$read_pickle(filename)
  
  return(pickle_data)
}