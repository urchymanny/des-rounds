s_boxes = [
    [ # sbox-1
      ["14","04",13,"01","02",15,11,"08","03",10,"06",12,"05","09","00","07"],
      ["00",15,"07","04",14,"02",13,10,"03","06",12,11,"09","05","03","08"],
      ["04","01",14,"08",13,"06","02",11,15,12,"09","07","03",10,"05","00"],
      [15,12,"08","02","04","09","01","07","05",11,"03",14,10,"00","06",13]
    ],
    [ # sbox-2 incorrect
      ["14","04",13,"01","02",15,11,"08","03",10,"06",12,"05","09","00","07"],
      ["00",15,"07","04",14,"02",13,10,"03","06",12,11,"09","05","03","08"],
      ["04","01",14,"08",13,"06","02",11,15,12,"09","07","03",10,"05","00"],
      [15,12,"08","02","04","09","01","07","05",11,"03",14,10,"00","06",13]
    ]]

R = ["1010","1110", "1001","1011", "0101", "1101", "0111", "0110"]
KEY = ["101010", "010011", "100011", "110011", "101011", "110101", "000101", "010110"]


def des_round_function(r,k,s):


  def expander(initial):
    inner_list = []

    def expand_item(item, prev, next):
      new_item = list(item)
      new_item = [list(prev)[-1]] + new_item + [list(next)[0]]
      re = "".join(new_item)
      return re

    new_list = []

    for i, item in enumerate(initial[1:-1]):
      if i == 0:
        prev = initial[0]
      else:
        prev = initial[1:-1][i-1]

      if i == (len(initial[1:-1]) - 1):
        next_item = initial[-1]
      else:
        next_item = initial[1:-1][i+1]
      new_item = expand_item(item, prev, next_item)
      new_list.append(new_item)

    first_item = expand_item(initial[0], initial[-1], initial[1])
    last_item = expand_item(initial[-1], initial[-2], initial[0])
    final_list = [first_item] + new_list +[last_item]
    print("Expanded List:", final_list)
    
    return final_list


  def xor_e_k(expanded_item, matching_key):
    e_list = list(expanded_item)
    k_item = list(matching_key)
    xor_list = []
    for i, item in enumerate(e_list):
      xor = '1' if item != k_item[i] else '0'
      # xor_list.append(f"{int(item) + int(k_item[i]) % 1}")
      xor_list.append(xor)
    re = "".join(xor_list)
    return re


  def make_r_k_xor_list(r, k):
    new_list = []
    for i, item in enumerate(expanded_R):
      xor_value = xor_e_k(item, k[i])
      new_list.append(xor_value)
    
    print("E XOR K:", new_list)
    return new_list


  def s_box_values(item, box_id, sboxes):
    item_list = list(item)
    row_binary = "".join([item_list[0]] + [item_list[-1]])
    col_binary = "".join(item_list[1:-1])

    print(f"S Box {box_id+1}, Row: {int(row_binary, 2)}, Column: {int(col_binary, 2)} = {sboxes[box_id][int(row_binary, 2)][int(col_binary, 2)]}")
    result = sboxes[box_id][int(row_binary, 2)][int(col_binary, 2)]
    return result

  

  def xor_sb_values(xor_e_r,sboxes):
    new_list = []
    print("----------")
    for item in xor_e_r:
      v = s_box_values(item, 0, sboxes)
      new_list.append(v)
      print("----------")
    return new_list

  expanded_R = expander(r)
  xor_list = r_k_xor_list(expanded_R, k)
  results = xor_sb_values(xor_list,s)

  return results


des_round_function(R,KEY,s_boxes)
