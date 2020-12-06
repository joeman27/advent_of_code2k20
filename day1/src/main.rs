use std::fs;

fn main(){
    let path = "../files/day1.txt";
    let contents: Vec<&str> = fs::read_to_string(path).unwrap().split("\n").collect();
    let mut res: u32;

    for line in contents{
        for line2 in contents{
            if line.parse::<u32>().unwrap() + line2.parse::<u32>().unwrap() == 2020{
                res = line.parse::<u32>().unwrap() * line2.parse::<u32>().unwrap();
            }

        }
    }
}