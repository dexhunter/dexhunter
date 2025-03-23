use macro_derive::{Languages, Hobbies, IndustryFocus, AcademicInterests};

pub trait Languages {}
pub trait Hobbies {}
pub trait IndustryFocus {}
pub trait AcademicInterests {}

#[derive(Debug, Languages, Hobbies, IndustryFocus, AcademicInterests)]
#[allow(dead_code)]
struct ReadMe {
    name: &'static str,
    blog: &'static str,
    email: &'static str,
    industry_focus: &'static str,
    academic_interests: &'static str,
    hobbies: &'static str,
}

const DEX: ReadMe = ReadMe {
    name: "Dex Hunter",
    blog: "https://dex.moe",
    email: "i@dex.moe",
    industry_focus: "web3/crypto, fintech, data science, llm/agentic system",
    academic_interests: "Deep Learning, Reinforcement Learning, Internet of Things, Distributed ledger Technology",
    hobbies: "weightlifting 🏋️‍♂️, guitars 🎸(particularly love surf🏄rock🪨), running🏃"
};

fn main() {
    println!("{:#?}", DEX);
}