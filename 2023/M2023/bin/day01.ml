open Core

let process line =
  printf "line: %s\n" line;
  let chars =
    String.filter line ~f:(fun c ->
      match c with
      | '1' .. '9' -> true
      | _ -> false)
  in
  let chars = Char.escaped chars.[0] ^ Char.escaped chars.[String.length chars - 1] in
  print_endline ("chars: " ^ chars);
  let line_calib = Int.of_string chars in
  printf "line_calib: %i\n" line_calib;
  print_endline "====================";
  line_calib
;;

let () =
  print_endline "\n\n====================";
  let file = "data/part2-testing.txt" in
  let ic = In_channel.create file in
  try
    let lines = In_channel.input_lines ic in
    let calibs = List.map lines ~f:process in
    let final_calib = List.fold calibs ~init:0 ~f:( + ) in
    print_endline ("final_calib: " ^ Int.to_string final_calib);
    print_endline "====================\n";
    In_channel.close ic
  with
  | e ->
    In_channel.close ic;
    raise e
;;
