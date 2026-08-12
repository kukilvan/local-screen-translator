from translation_pipeline import TranslationPipeline


pipeline = TranslationPipeline()

try:
    result = pipeline.translate_with_alignment(
        "Not even a groan? How disappointing.",
        "groan",
    )

    print("SOURCE:")
    print(result["source_text"])

    print("\nTRANSLATION:")
    print(result["translation"])

    print("\nWORD:")
    print(
        f'{result["source_word"]} -> '
        f'{result["target_phrase"]}'
    )

    print("\nINDICES:")
    print(result["target_indices"])

finally:
    pipeline.close()
