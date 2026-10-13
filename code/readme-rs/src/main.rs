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
    blog: "https://blog.dex.moe",
    email: "i@dex.moe",
    industry_focus: "recursively self-improving AI agents, LLM/agentic systems (earlier: web3/crypto, fintech, data science)",
    academic_interests: "Recursive Self-Improvement, AI Research Agents, Tree Search over Code, Deep Learning, Reinforcement Learning (earlier: Internet of Things, Distributed Ledger Technology)",
    hobbies: "weightlifting 🏋️‍♂️, guitars 🎸 (particularly love surf rock 🏄🪨)"
};

fn main() {
    println!("{:#?}", DEX);
}