use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(Languages)]
pub fn languages_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    
    let expanded = quote! {
        impl Languages for #name {}
    };
    
    TokenStream::from(expanded)
}

#[proc_macro_derive(Hobbies)]
pub fn hobbies_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    
    let expanded = quote! {
        impl Hobbies for #name {}
    };
    
    TokenStream::from(expanded)
}

#[proc_macro_derive(IndustryFocus)]
pub fn industry_focus_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    
    let expanded = quote! {
        impl IndustryFocus for #name {}
    };
    
    TokenStream::from(expanded)
}

#[proc_macro_derive(AcademicInterests)]
pub fn academic_interests_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = &input.ident;
    
    let expanded = quote! {
        impl AcademicInterests for #name {}
    };
    
    TokenStream::from(expanded)
}