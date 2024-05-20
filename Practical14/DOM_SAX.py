import xml.dom.minidom
import matplotlib.pyplot as plt

def parse_with_dom(file_path):
    DOMTree = xml.dom.minidom.parse(file_path)
    terms = DOMTree.getElementsByTagName('term')
    molecular_function = 0
    biological_process = 0
    cellular_component = 0

    for term in terms:
        namespaces = term.getElementsByTagName('namespace')
        for namespace in namespaces:
            ontology = namespace.firstChild.nodeValue.strip()
            if ontology == 'molecular_function':
                molecular_function += 1
            elif ontology == 'biological_process':
                biological_process += 1
            elif ontology == 'cellular_component':
                cellular_component += 1

    # save result to the dictionary
    results = {
        'Molecular function': molecular_function,
        'Biological process': biological_process,
        'Cellular component': cellular_component
    }

    # draw the bar chart
    ontologies = list(results.keys())
    counts = list(results.values())
    plt.bar(ontologies, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.title('Number of GO Terms by Ontology (DOM)')
    plt.show()

    
    return results

# use function and print the result
file_path = r'C:\Users\Lenovo\Downloads'  
go_term_counts = parse_with_dom(file_path)
for ontology, count in go_term_counts.items():
    print(f"{ontology} (DOM): {count}")