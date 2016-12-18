import sys,os,pkgutil

def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module

def main():
    load_all_modules_from_dir('Laboratorio_1')
    load_all_modules_from_dir('laboratorio_2')
    load_all_modules_from_dir('Laboratorio_3')
    load_all_modules_from_dir('laboratorio_3b')
    load_all_modules_from_dir('laboratorio_4')
    print "Archivo principal"

if __name__ == '__main__':
        main()
