import gql from "graphql-tag";

export const getCountries = gql`
    query countries{
        countries {
            name
        }
    }`;