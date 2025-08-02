#!/usr/bin/env python3
"""
RCSB PDB API Query Script

This script demonstrates how to use the rcsb-api library to perform
a full_text search on the RCSB Protein Data Bank.
"""

from rcsbapi.search import TextQuery


def main():
    """Perform a full_text search for isopeptide + (collagen | fibrinogen)"""
    
    # Define the search query
    search_term = "isopeptide + ( collagen | fibrinogen )"
    
    print(f"Searching RCSB PDB for: {search_term}")
    print("=" * 60)
    
    try:
        # Create a text query for full text search
        query = TextQuery(search_term)
        
        # Execute the search - the query object itself is callable
        results = list(query())
        
        # Display results
        if results:
            print(f"Found {len(results)} entries:")
            print("-" * 40)
            
            for i, pdb_id in enumerate(results, 1):
                print(f"{i:3d}. PDB ID: {pdb_id}")
                
            print("-" * 40)
            print(f"Total entries found: {len(results)}")
            
        else:
            print("No results found for the given search term.")
            
    except Exception as e:
        print(f"Error occurred during search: {e}")
        print("Please ensure you have internet connectivity and the rcsb-api library is properly installed.")


if __name__ == "__main__":
    main()