import subprocess

def test_lesson_05():
    result = subprocess.run(['python3', 'lesson_05.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert output[0].startswith("10"), f"Failed TODO 1: {output[0]}"
    assert "Hello" in output[1], f"Failed TODO 2: {output[1]}"
    assert "30 years old" in output[2], f"Failed TODO 3: {output[2]}"
    assert output[3] == "15", f"Failed TODO 4: {output[3]}"
    assert "age" in output[4], f"Failed TODO 5: {output[4]}"
    assert "20" in output[5], f"Failed TODO 6: {output[5]}"
    assert "city" in output[6], f"Failed TODO 7: {output[6]}"
    assert "30" in output[7], f"Failed TODO 8: {output[7]}"
    assert "Annotations" in output[8], f"Failed TODO 9: {output[8]}"
    assert "fixed" in output[9], f"Failed TODO 10: {output[9]}"

    print("Lesson 5: All tests passed!")

if __name__ == "__main__":
    test_lesson_05()
