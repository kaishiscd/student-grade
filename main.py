def calculate_final_grade(scores):
    if not scores:
        raise ValueError("minimal harus ada satu nilai.")

    for category, score in scores.items():
        if not isinstance(score, (int, float)) or not 0 <= score <= 100:
            raise ValueError(f"nilai {category} harus ada di antara 0 sampai 100.")

    return sum(scores.values()) / len(scores)


def get_letter_grade(final_score):
    if final_score >= 90:
        return "A"
    elif final_score >= 80:
        return "B"
    elif final_score >= 70:
        return "C"
    elif final_score >= 60:
        return "D"
    return "E"


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    student_name = input("Nama siswa: ").strip()
    if not student_name:
        student_name = "Siswa"

    categories = ["Tugas", "Kuis", "UTS", "UAS"]
    scores = {}

    for category in categories:
        while True:
            try:
                score = float(input(f"Nilai {category} (0-100): "))
                if not 0 <= score <= 100:
                    print("masukkan nilai dari 0 sampai 100.")
                    continue
                scores[category] = score
                break
            except ValueError:
                print("input gak valid. masukkan angka, misalnya 85.")

    final_score = calculate_final_grade(scores)
    letter_grade = get_letter_grade(final_score)
    status = "LULUS" if final_score >= 70 else "BELUM LULUS"

    print("\n" + "-" * 40)
    print("             HASIL NILAI")
    print("-" * 40)
    print(f"Nama siswa  : {student_name}")
    for category, score in scores.items():
        print(f"{category:<12}: {score:.2f}")
    print("-" * 40)
    print(f"Nilai akhir : {final_score:.2f}")
    print(f"Grade       : {letter_grade}")
    print(f"Status      : {status}")
    print("-" * 40)


if __name__ == "__main__":
    main()
