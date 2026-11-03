import sys, argparse
try:
    from .core import cross_reference_documents
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_ai_cross_reference.core import cross_reference_documents
    from pdfjin_ai_cross_reference import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-ai-cross-reference", description="Cross-reference multiple PDFs.")
    p.add_argument("docs", nargs="+", help="PDF documents to cross-reference")
    p.add_argument("-q", "--query", required=True, help="Research question or topic")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        print(cross_reference_documents(args.docs, query=args.query))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
