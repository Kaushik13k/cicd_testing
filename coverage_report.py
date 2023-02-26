import coverage

cov = coverage.Coverage()
cov.load()

# Get the coverage percentage
coverage_percentage = cov.report()

print(f"Code coverage percentage: {coverage_percentage:.2f}%")
